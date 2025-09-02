-- 1. class_master
CREATE TABLE class_master (
    id SERIAL PRIMARY KEY,
    name INTEGER NOT NULL,
    is_board BOOLEAN NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 2. students
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    admission_number VARCHAR(20) NOT NULL UNIQUE,
    admission_date TIMESTAMP WITH TIME ZONE NOT NULL,
    phone_number VARCHAR(15),
    student_email VARCHAR(255),
    dob DATE NOT NULL,
    address TEXT NOT NULL,
    classes_id INTEGER NOT NULL REFERENCES class_master(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 3. parents
CREATE TABLE parents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    dob DATE NOT NULL,
    occupation VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 4. subject_master
CREATE TABLE subject_master (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    code VARCHAR(50) NOT NULL UNIQUE,
    description TEXT,
    subject_type VARCHAR(20),
    credits INTEGER,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 5. teachers
CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    teacher_email VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    joining_date DATE NOT NULL,
    qualifications VARCHAR(20) NOT NULL,
    role VARCHAR(20) NOT NULL,
    primary_specialization_id INTEGER NOT NULL REFERENCES subject_master(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 6. student_parent_mapping
CREATE TABLE student_parent_mapping (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    parent_id INTEGER NOT NULL REFERENCES parents(id) ON DELETE CASCADE,
    relationship VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    CONSTRAINT unique_student_parent_mapping UNIQUE (student_id, parent_id)
);

CREATE INDEX idx_student_parent_mapping_student_id ON student_parent_mapping(student_id);
CREATE INDEX idx_student_parent_mapping_parent_id ON student_parent_mapping(parent_id);

-- 7. student_subject_mapping
CREATE TABLE student_subject_mapping (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    subject_id INTEGER NOT NULL REFERENCES subject_master(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 8. teacher_subject_class_mapping
CREATE TABLE teacher_subject_class_mapping (
    id SERIAL PRIMARY KEY,
    classes_id INTEGER NOT NULL REFERENCES class_master(id) ON DELETE CASCADE,
    teacher_id INTEGER NOT NULL REFERENCES teachers(id) ON DELETE CASCADE,
    subject_id INTEGER NOT NULL REFERENCES subject_master(id) ON DELETE CASCADE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    CONSTRAINT unique_teacher_subject_class UNIQUE (teacher_id, subject_id, classes_id)
);
