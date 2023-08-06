import abc
import inspect
import json
import sys
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any
from typing import Callable
from typing import Literal
from typing import NamedTuple
from typing import Optional
from typing import Sequence
from typing import Type
from typing import TypeVar
from typing import Union
from typing import get_origin

from pydantic import BaseModel
from pydantic import Field
from pydantic import create_model

from gwproto.message import Header
from gwproto.message import Message
from gwproto.topic import MQTTTopic


class Decoder(abc.ABC):
    def decode_str(self, content: str | bytes, encoding: str = "utf-8") -> Any:
        if isinstance(content, bytes):
            content = content.decode(encoding)
        return self.decode_obj(json.loads(content))

    @abstractmethod
    def decode_obj(self, o: Any) -> Any:
        ...


class CallableDecoder(Decoder):
    _decode_obj: Callable[[Any], Any]

    def __init__(self, decode_obj: Callable[[Any], Any]):
        if not callable(decode_obj):
            raise ValueError(
                f"ERROR. decode_obj {decode_obj}/{type(decode_obj)} attribute is not Callable"
            )
        self._decode_obj = decode_obj

    def decode_obj(self, o: Any) -> Any:
        return self._decode_obj(o)


class PydanticDecoder(CallableDecoder):
    def __init__(self, model: Type["BaseModel"]):
        super().__init__(model.parse_obj)


class MakerDecoder(CallableDecoder):
    DECODER_FUNCTION_NAME: str = "dict_to_tuple"

    def __init__(self, model: Any):
        decoder_function = getattr(model, self.DECODER_FUNCTION_NAME, None)
        if decoder_function is None:
            raise ValueError(
                f"ERROR. {model} has no function {self.DECODER_FUNCTION_NAME}"
            )
        super().__init__(decoder_function)


MessageDiscriminator = TypeVar("MessageDiscriminator", bound=Message[Any])


class MessageDecoder(Decoder):
    decoders: "Decoders"
    message_payload_discriminator: Optional[MessageDiscriminator]

    def __init__(
        self,
        decoders: "Decoders",
        message_payload_discriminator: Optional[Type[MessageDiscriminator]] = None,
    ):
        self.decoders = decoders
        self.message_payload_discriminator = message_payload_discriminator

    def decode_obj(self, o: Any) -> Message[Any]:
        message_dict: dict = dict(o)
        message_dict["Header"] = Header.parse_obj(message_dict.get("Header", dict()))
        message: Message[Any]
        if message_dict["Header"].MessageType in self.decoders:
            message_dict["Payload"] = self.decoders.decode_obj(
                message_dict["Header"].MessageType,
                message_dict.get("Payload", dict()),
            )
            message = Message(**message_dict)
        else:
            message = self.message_payload_discriminator.parse_obj(message_dict)
        return message


class DecoderItem(NamedTuple):
    type_name: str
    decoder: Decoder


DEFAULT_TYPE_NAME_FIELD = "TypeName"


@dataclass
class OneDecoderExtractor:
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD
    decoder_function_name: str = "parse_obj"

    def get_type_name(self, obj: Any) -> str:
        if not (type_name := getattr(obj, self.type_name_field, "")):
            if (decoder_fields := getattr(obj, "__fields__", None)) is not None:
                if (
                    model_field := decoder_fields.get(self.type_name_field, None)
                ) is not None:
                    type_name = getattr(model_field, "default", "")
        return type_name

    def get_decoder(self, obj: Any) -> Optional[Decoder]:
        decoder_function = getattr(obj, self.decoder_function_name, None)
        if callable(decoder_function):
            decoder = CallableDecoder(decoder_function)
        else:
            decoder = None
        return decoder

    def extract(self, obj: Any) -> Optional[DecoderItem]:
        item = None
        if type_name := self.get_type_name(obj):
            if (decoder := self.get_decoder(obj)) is not None:
                item = DecoderItem(type_name, decoder)
        return item


@dataclass
class MakerExtractor(OneDecoderExtractor):
    type_name_field: str = "type_alias"
    decoder_function_name: str = MakerDecoder.DECODER_FUNCTION_NAME


class Decoders:
    _decoders: dict[str, Decoder]

    def __init__(self, decoders: Optional[dict[str, Decoder]] = None):
        self._decoders = dict()
        if decoders is not None:
            self.add_decoders(decoders)

    def decoder(self, type_name: str) -> Decoder:
        return self._decoders[type_name]

    def decode_str(self, type_name: str, content: str | bytes, encoding="utf-8") -> Any:
        return self.decoder(type_name).decode_str(content, encoding=encoding)

    def decode_obj(self, type_name: str, o: Any) -> Any:
        return self.decoder(type_name).decode_obj(o)

    def add_decoder(self, type_name: str, decoder: Decoder) -> "Decoders":
        self._validate(type_name, decoder)
        self._decoders[type_name] = decoder
        return self

    def add_decoders(self, decoders: dict[str, Decoder]) -> "Decoders":
        for type_name, decoder in decoders.items():
            self._validate(type_name, decoder)
        self._decoders.update(decoders)
        return self

    def merge(self, other: "Decoders") -> "Decoders":
        self.add_decoders(other._decoders)
        return self

    def __contains__(self, type_name: str) -> bool:
        return type_name in self._decoders

    def types(self) -> list[str]:
        return list(self._decoders.keys())

    def _validate(self, type_name: str, decoder: Decoder) -> None:
        if type_name in self._decoders:
            if self._decoders[type_name] is not decoder:
                raise ValueError(
                    f"ERROR. decoder for [{type_name}] is already present as [{self._decoders[type_name]}]"
                )

    @classmethod
    def from_objects(
        cls,
        objs: Optional[list[Any]] = None,
        message_payload_discriminator: Optional[Type[MessageDiscriminator]] = None,
        extractors: Optional[Sequence[OneDecoderExtractor]] = None,
    ) -> "Decoders":
        items = dict()
        if objs is not None:
            if extractors is None:
                extractors = [OneDecoderExtractor(), MakerExtractor()]
            for obj in objs:
                for extractor in extractors:
                    item = extractor.extract(obj)
                    if item is not None:
                        items[item.type_name] = item.decoder
                        break
        d = Decoders(items)
        d.add_decoder(
            Message.type_name(), MessageDecoder(d, message_payload_discriminator)
        )
        return d


class MQTTCodec(abc.ABC):
    ENCODING = "utf-8"
    decoders: Decoders

    def __init__(self, decoders: Decoders):
        self.decoders = Decoders().merge(decoders)
        super().__init__()

    def encode(self, content: Any) -> bytes:
        if isinstance(content, bytes):
            encoded = content
        else:
            encoded = content.json()
            if not isinstance(encoded, bytes):
                encoded = encoded.encode(self.ENCODING)
        return encoded

    def decode(self, topic: str, payload: bytes) -> Any:
        decoded_topic = MQTTTopic.decode(topic)
        if decoded_topic.envelope_type not in self.decoders:
            raise Exception(
                f"Type {decoded_topic.envelope_type} not recognized. Available decoders: {self.decoders.types()}"
            )
        self.validate_source_alias(decoded_topic.src)
        return self.decoders.decode_str(
            decoded_topic.envelope_type, payload, encoding=self.ENCODING
        )

    @abstractmethod
    def validate_source_alias(self, source_alias: str):
        ...


def get_pydantic_literal_type_name(
    o: Any, type_name_field: str = DEFAULT_TYPE_NAME_FIELD
) -> str:
    if hasattr(o, "__fields__"):
        if type_name_field in o.__fields__:
            if get_origin(o.__fields__[type_name_field].annotation) == Literal:
                return str(o.__fields__[type_name_field].default)
    return ""


def pydantic_named_types(
    module_names: str | Sequence[str],
    modules: Optional[Sequence[Any]] = None,
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
) -> list[Any]:
    if isinstance(module_names, str):
        module_names = [module_names]
    if unimported := [
        module_name for module_name in module_names if not module_name in sys.modules
    ]:
        raise ValueError(f"ERROR. modules {unimported} have not been imported.")
    named_types = []
    type_names: dict[str, Any] = dict()
    if modules is None:
        modules = []
    for module in [sys.modules[module_name] for module_name in module_names] + list(
        modules
    ):
        module_classes = [
            entry[1] for entry in inspect.getmembers(module, inspect.isclass)
        ]
        for module_class in module_classes:
            if type_name := get_pydantic_literal_type_name(
                module_class, type_name_field=type_name_field
            ):
                if type_name in type_names:
                    raise ValueError(
                        f"ERROR {type_name_field} ({type_name}) "
                        f"for {module_class} already seen for "
                        f"class {type_names[type_name]}"
                    )
                type_names[type_name] = module_class
                named_types.append(module_class)
    return named_types


def create_message_payload_discriminator(
    model_name: str,
    module_names: str | Sequence[str] = "",
    modules: Optional[Sequence[Any]] = None,
    explicit_types: Optional[Sequence[Any]] = None,
    type_name_field: str = DEFAULT_TYPE_NAME_FIELD,
) -> Type[MessageDiscriminator]:
    used_types = pydantic_named_types(module_names=module_names, modules=modules)
    if explicit_types is not None:
        used_types.extend(explicit_types)
    return create_model(
        model_name,
        __base__=Message,  # type: ignore
        Payload=(
            Union[tuple(used_types)],
            Field(..., discriminator=type_name_field),
        ),
    )
