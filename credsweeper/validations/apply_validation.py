from multiprocessing import Pool
from typing import List

from credsweeper.common.constants import KeyValidationOption
from credsweeper.credentials import Candidate, CredentialManager
from credsweeper.logger.logger import logging


class ApplyValidation:
    """Class that allow parallel API validation using already declared pool."""

    def validate_credentials(self, pool: Pool, credential_manager: CredentialManager) -> None:
        old_cred: List[Candidate] = credential_manager.get_credentials()
        new_cred = []
        validations: List[KeyValidationOption] = pool.map(self.validate, old_cred)
        for cred, validation in zip(old_cred, validations):
            cred.api_validation = validation
            new_cred.append(cred)

        credential_manager.set_credentials(new_cred)

    def validate(self, cred: Candidate) -> KeyValidationOption:
        """Iterate over all `validations` in current cred.

        If any validation results in VALIDATED_KEY - final result is VALIDATED_KEY
        If no VALIDATED_KEY, but at least one INVALID_KEY - final result is INVALID_KEY
        UNDECIDED otherwise
        """
        validation_option = KeyValidationOption.UNDECIDED

        if not cred.is_api_validation_available:
            logging.debug(f"No validation with external API available for current credential candidate: "
                          f"{cred.line_data_list[0].line}")
            return KeyValidationOption.NOT_AVAILABLE

        for validation in cred.validations:
            current_api_validation: KeyValidationOption = validation.verify(cred.line_data_list)
            if current_api_validation is KeyValidationOption.VALIDATED_KEY:
                logging.debug(
                    f"Valid validation by: {validation.__class__.__name__} for line: {cred.line_data_list[0].line}")
                validation_option = current_api_validation
                break
            if current_api_validation is KeyValidationOption.INVALID_KEY:
                logging.debug(
                    f"Invalid validation by: {validation.__class__.__name__} for line: {cred.line_data_list[0].line}")
                validation_option = current_api_validation

        return validation_option
