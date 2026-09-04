import pytest
from conftest import get_db, engine
from models import Student, Base


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)

    with engine.begin() as conn:
        conn.execute(Student.__table__.delete())

    db = next(get_db())
    try:
        yield db
    finally:
        db.rollback()
        db.close()


def test_add_student(db_session):
    new_student = Student(
        level="Upper-Intermediate",
        education_form="personal",
        subject_id=999,
    )
    db_session.add(new_student)
    db_session.commit()

    assert new_student.user_id is not None
    assert new_student.level == "Upper-Intermediate"


def test_update_student(db_session):
    student = Student(
        level="Beginner",
        education_form="group",
        subject_id=998,
    )
    db_session.add(student)
    db_session.commit()

    student_id = student.user_id
    assert student_id is not None

    student.level = "Advanced"
    db_session.commit()

    updated = (
        db_session.query(Student)
        .filter(Student.user_id == student_id)
        .first()
    )
    assert updated is not None
    assert updated.level == "Advanced"


def test_delete_student(db_session):
    student = Student(
        level="ToDelete",
        education_form="group",
        subject_id=997,
    )
    db_session.add(student)
    db_session.commit()

    user_id = student.user_id

    db_session.delete(student)
    db_session.commit()

    deleted = (
        db_session.query(Student)
        .filter(Student.user_id == user_id)
        .first()
    )
    assert deleted is None
