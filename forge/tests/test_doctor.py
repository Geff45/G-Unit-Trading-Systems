from forge.commands.doctor import DoctorCommand


def test_doctor_command():

    doctor = DoctorCommand()

    assert doctor is not None

    assert hasattr(doctor, "run")


def test_virtual_environment():

    doctor = DoctorCommand()

    assert isinstance(
        doctor.virtual_environment(),
        bool,
    )


def test_git_repository():

    from pathlib import Path

    doctor = DoctorCommand()

    assert isinstance(
        doctor.git_repository(Path.cwd()),
        bool,
    )