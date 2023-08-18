def user_course_photo_upload_path(instance, filename):
    return f'users/{instance.pk}/courses/preview/{filename}'


def user_courses_upload_path(instance, filename):
    return f'users/{instance.pk}/courses/videos/{filename}'
