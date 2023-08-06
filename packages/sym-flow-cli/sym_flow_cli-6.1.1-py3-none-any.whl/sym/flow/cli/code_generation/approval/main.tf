locals {
  environment_name = "main"
}

provider "sym" {
  org = "${var.sym_org_slug}"
}

resource "sym_flow" "this" {
  name  = "approval"
  label = "Approval"

  implementation = "${path.module}/impl.py"
  environment_id = sym_environment.this.id

  params {
    # If you want a Flow with an escalation strategy, add your strategy_id here!
    # strategy_id = ...

    # The prompt_field block defines a custom form field for the Slack modal that
    # requesters fill out to make their requests.
    prompt_field {
      name = "galaxy-name"
      label = "Which galaxy would you like to travel to?"
      type = "string"
      required = true
      allowed_values = ["Andromeda Galaxy", "Triangulum Galaxy", "Wolf–Lundmark–Melotte"]
    }

    prompt_field {
      name = "reason"
      label = "Why would you like to go?"
      type = "string"
      required = true
    }
  }
}

# The sym_environment is a container for sym_flows that share configuration values
# (e.g. shared integrations or error logging)
resource "sym_environment" "this" {
  name            = local.environment_name
  error_logger_id = sym_error_logger.slack.id

  integrations = {
    slack_id = sym_integration.slack.id

    # Add your integration IDs here!
  }
}

resource "sym_integration" "slack" {
  type = "slack"
  name = "${local.environment_name}-slack"

  external_id = "${var.slack_workspace_id}"
}

# This sym_error_logger will output any warnings and errors that occur during
# execution of a sym_flow to a specified channel in Slack.
resource "sym_error_logger" "slack" {
  integration_id = sym_integration.slack.id

  # Make sure that this channel has been created in your workspace
  destination    = "#sym-errors"
}
