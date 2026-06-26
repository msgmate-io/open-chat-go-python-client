from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.n8n_trigger_workflow_webhook_call_input_parameters import N8NTriggerWorkflowWebhookCallInputParameters





T = TypeVar("T", bound="N8NTriggerWorkflowWebhookCall")



@_attrs_define
class N8NTriggerWorkflowWebhookCall:
    """ The parameters for the tool

        Attributes:
            input_parameters (N8NTriggerWorkflowWebhookCallInputParameters): The input parameters to send to the n8n webhook
                as a JSON object
     """

    input_parameters: N8NTriggerWorkflowWebhookCallInputParameters
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.n8n_trigger_workflow_webhook_call_input_parameters import N8NTriggerWorkflowWebhookCallInputParameters
        input_parameters = self.input_parameters.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "input_parameters": input_parameters,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.n8n_trigger_workflow_webhook_call_input_parameters import N8NTriggerWorkflowWebhookCallInputParameters
        d = dict(src_dict)
        input_parameters = N8NTriggerWorkflowWebhookCallInputParameters.from_dict(d.pop("input_parameters"))




        n8n_trigger_workflow_webhook_call = cls(
            input_parameters=input_parameters,
        )


        n8n_trigger_workflow_webhook_call.additional_properties = d
        return n8n_trigger_workflow_webhook_call

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
