from __future__ import annotations

from enum import StrEnum


class ToolName(StrEnum):
    CREATE_CONFIRMABLE_ACTION_SUGGESTION = 'create_confirmable_action_suggestion'
    GET_CURRENT_TIME = 'get_current_time'
    GET_CURRENT_TIME_CONFIRMED = 'get_current_time_confirmed'
    GET_CURRENT_TIME_CONFIRMED_TESTING = 'get_current_time_confirmed_testing'
    GET_RANDOM_NUMBER = 'get_random_number'
    GET_WEATHER = 'get_weather'
    LITTLE_WORLD_CHAT_REPLY = 'little_world__chat_reply'
    LITTLE_WORLD_GENERATE_MESSAGE_REPLY_SUGGESTION = 'little_world__generate_message_reply_suggestion'
    LITTLE_WORLD_GET_PAST_MESSAGES = 'little_world__get_past_messages'
    LITTLE_WORLD_GET_USER_STATE = 'little_world__get_user_state'
    LITTLE_WORLD_RESOLVE_MATCH = 'little_world__resolve_match'
    LITTLE_WORLD_RETRIEVE_MATCH_OVERVIEW = 'little_world__retrieve_match_overview'
    LITTLE_WORLD_SET_USER_SEARCHING_STATE = 'little_world__set_user_searching_state'
    N8N_TRIGGER_WORKFLOW_WEBHOOK = 'n8n_trigger_workflow_webhook'
    RUN_CALLBACK_FUNCTION = 'run_callback_function'
    RWTH_AACHEN_SEMINAR_TIMS_AUTO_PAPER_INCLUDE_EXCLUDE = 'rwth_aachen_seminar_tims_auto_paper_include_exclude'
    TOOL_INIT_TEST_TOOL_PASS_THROUGH = 'tool_init_test_tool_pass_through'
