from django.conf import settings


# Certifications roles
ROL_CH_EXO_FOUNDATIONS = settings.EXO_ROLE_CODE_CERTIFICATION_FOUNDATIONS
ROL_CH_AMBASSADOR = settings.EXO_ROLE_CODE_CERTIFICATION_AMBASSADOR
ROL_CH_COACH = settings.EXO_ROLE_CODE_CERTIFICATION_SPRINT_COACH
ROL_CH_CONSULTANT = settings.EXO_ROLE_CODE_CERTIFICATION_CONSULTANT
ROL_CH_EXO_TRAINER = settings.EXO_ROLE_CODE_CERTIFICATION_TRAINER
ROL_CH_BOARD_ADVISOR = settings.EXO_ROLE_CODE_CERTIFICATION_BOARD_ADVISOR


CERTIFICATION_REQUIREMENTS = {
    # EXO SPRINT
    settings.EXO_ROLE_CODE_SPRINT_HEAD_COACH: [ROL_CH_COACH],
    settings.EXO_ROLE_CODE_SPRINT_COACH: [ROL_CH_COACH],
    settings.EXO_ROLE_CODE_AWAKE_SPEAKER: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_ALIGN_TRAINER: [ROL_CH_EXO_TRAINER],
    settings.EXO_ROLE_CODE_ADVISOR: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_DISRUPTOR: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_DISRUPTOR_SPEAKER: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_DELIVERY_MANAGER: [],
    settings.EXO_ROLE_CODE_SPRINT_PARTICIPANT: [],
    settings.EXO_ROLE_CODE_SPRINT_CONTRIBUTOR: [],
    settings.EXO_ROLE_CODE_SPRINT_REPORTER: [],
    settings.EXO_ROLE_CODE_ACCOUNT_MANAGER: [],
    settings.EXO_ROLE_CODE_SHADOW_COACH: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_SPRINT_OTHER: [],

    # FASTRACK
    settings.EXO_ROLE_CODE_FASTRACK_TEAM_LEADER: [],
    settings.EXO_ROLE_CODE_FASTRACK_TEAM_MEMBER: [],
    settings.EXO_ROLE_CODE_FASTRACK_CURATOR: [],
    settings.EXO_ROLE_CODE_FASTRACK_CO_CURATOR: [],
    settings.EXO_ROLE_CODE_FASTRACK_SOLUTION_ACCELERATOR: [],
    settings.EXO_ROLE_CODE_FASTRACK_OBSERVER_EVALUATOR: [],
    settings.EXO_ROLE_CODE_FASTRACK_LOCAL_TEAM_MEMBER: [],

    # WORKSHOP
    settings.EXO_ROLE_CODE_WORKSHOP_SPEAKER: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_WORKSHOP_TRAINER: [ROL_CH_EXO_TRAINER],

    # SWARM
    settings.EXO_ROLE_CODE_SWARM_ADVISOR: [ROL_CH_EXO_FOUNDATIONS],

    # SUMMITS
    settings.EXO_ROLE_CODE_SUMMIT_COLLABORATOR: [],
    settings.EXO_ROLE_CODE_SUMMIT_SPEAKER: [],
    settings.EXO_ROLE_CODE_SUMMIT_FACILITATOR: [],
    settings.EXO_ROLE_CODE_SUMMIT_ORGANIZER: [],

    # TICKET
    settings.EXO_ROLE_CODE_TICKET_ADVISOR: [ROL_CH_EXO_FOUNDATIONS],

    # TALK
    settings.EXO_ROLE_CODE_TALK_SPEAKER: [ROL_CH_EXO_FOUNDATIONS],

    # DISRUPTION SESION
    settings.EXO_ROLE_CODE_DISRUPTION_SPEAKER: [ROL_CH_EXO_FOUNDATIONS],

    # OTHER
    settings.EXO_ROLE_CODE_OTHER_ADVISOR: [
        ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_OTHER_COACH: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_OTHER_CONSULTANT: [ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_OTHER_SPEAKER: [
        ROL_CH_EXO_FOUNDATIONS],
    settings.EXO_ROLE_CODE_OTHER_TRAINER: [ROL_CH_EXO_TRAINER],
    settings.EXO_ROLE_CODE_OTHER_OTHER: [],
    settings.EXO_ROLE_CODE_OTHER_DISRUPTOR: [
        ROL_CH_EXO_FOUNDATIONS]
}