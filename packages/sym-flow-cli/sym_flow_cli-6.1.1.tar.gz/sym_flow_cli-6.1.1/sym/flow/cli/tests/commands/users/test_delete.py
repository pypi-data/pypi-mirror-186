from unittest.mock import patch

from sym.flow.cli.symflow import symflow as click_command


class TestUsersDelete:
    @patch("sym.flow.cli.helpers.api.SymAPI.delete_user")
    def test_delete(self, mock_delete_user, click_setup):
        with click_setup() as runner:
            result = runner.invoke(click_command, ["users", "delete", "user@symops.io", "--force"])
            assert result.exit_code == 0

        mock_delete_user.assert_called_once()

    @patch("sym.flow.cli.helpers.api.SymAPI.delete_user")
    def test_delete_no_username_no_force(self, _, click_setup):
        with click_setup() as runner:
            with patch("inquirer.list_input") as mock_inquire:
                result = runner.invoke(click_command, ["users", "delete"])
                assert result.exit_code == 2

    @patch("sym.flow.cli.helpers.api.SymAPI.delete_user")
    def test_delete_no_force_no_confirm(self, _, click_setup):
        with click_setup() as runner:
            result = runner.invoke(click_command, ["users", "delete", "user@symops.io"])
            assert result.exit_code == 1

    @patch("sym.flow.cli.commands.users.delete.click.confirm", return_value=True)
    @patch("sym.flow.cli.helpers.api.SymAPI.delete_user")
    def test_delete_no_force_with_confirm(self, _, mock_delete_user, click_setup):
        with click_setup() as runner:
            result = runner.invoke(click_command, ["users", "delete", "user@symops.io"])
            assert result.exit_code == 0

    @patch("sym.flow.cli.helpers.api.SymAPI.delete_user")
    def test_delete_no_username_with_force(self, _, click_setup):
        with click_setup() as runner:
            result = runner.invoke(click_command, ["users", "delete", "--force"])
            assert result.exit_code == 2
