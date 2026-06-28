from __future__ import annotations

from enum import StrEnum


class ToolName(StrEnum):
    CREATE_CONFIRMABLE_ACTION_SUGGESTION = 'create_confirmable_action_suggestion'
    GET_CURRENT_TIME = 'get_current_time'
    GET_CURRENT_TIME_CONFIRMED = 'get_current_time_confirmed'
    GET_CURRENT_TIME_CONFIRMED_TESTING = 'get_current_time_confirmed_testing'
    GET_RANDOM_NUMBER = 'get_random_number'
    GET_WEATHER = 'get_weather'
    N8N_TRIGGER_WORKFLOW_WEBHOOK = 'n8n_trigger_workflow_webhook'
    RUN_CALLBACK_FUNCTION = 'run_callback_function'
    TOOL_INIT_TEST_TOOL_PASS_THROUGH = 'tool_init_test_tool_pass_through'
