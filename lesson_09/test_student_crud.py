import pytest
from conftest import get_db, engine
from models import Student, Base

@pytest.fixture(scope="function")
def db_session():
    # 1. Создаем таблицы, если их нет
    Base.metadata.create_all(bind=engine)
    
    # 2. ВАЖНО: Очищаем таблицу student от старых данных перед тестом!
    # Это предотвращает ошибку StaleDataError, если в базе остались строки.
    with engine.connect() as conn:
        conn.execute(Student.__table__.delete())
        conn.commit()

    # 3. Создаем сессию для теста
    db = next(get_db())
    try:
        yield db
    finally:
        # 4. Откат изменений, сделанных в самом тесте
        db.rollback()
        db.close()

def test_add_student(db_session):
    new_student = Student(
        level="Upper-Intermediate",
        education_form="personal",
        subject_id=999
    )
    db_session.add(new_student)
    db_session.commit()

    assert new_student.user_id is not None
    assert new_student.level == "Upper-Intermediate"

def test_update_student(db_session):
    # Создаем студента
    student = Student(
        level="Beginner",
        education_form="group",
        subject_id=998
    )
    db_session.add(student)
    db_session.commit()
    
    # Сохраняем ID, чтобы быть уверенными, что работаем с ним
    student_id = student.user_id
    assert student_id is not None

    # Обновляем данные
    student.level = "Advanced"
    db_session.commit()

    # Проверяем, что данные реально обновились в базе
    updated = db_session.query(Student).filter(Student.user_id == student_id).first()
    assert updated is not None
    assert updated.level == "Advanced"

def test_delete_student(db_session):
    student = Student(
        level="ToDelete",
        education_form="group",
        subject_id=997
    )
    db_session.add(student)
    db_session.commit()

    user_id = student.user_id
    
    # Удаляем
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что записи нет
    deleted = db_session.query(Student).filter(Student.user_id == user_id).first()
    assert deleted is None
