from openedx.core.release import RELEASE_LINE
GINKGO = 'ginkgo'
FICUS = 'ficus'
SUPPORTED_RELEASES = (GINKGO, FICUS)


def current_release():
    try:
        release = RELEASE_LINE
    except AttributeError:
        release = 'ficus'
    if release not in SUPPORTED_RELEASES:
        raise ValueError("Got unsupported edx release : '{}'".format(release))
    return release

release = current_release()

if release == GINKGO:
    from openedx.core.djangoapps.course_groups.cohorts import set_course_cohorted
    set_course_cohort_settings = lambda course_key, is_cohorted: set_course_cohorted(course_key, is_cohorted)
else:
    from openedx.core.djangoapps.course_groups.cohorts import set_course_cohort_settings

if release == GINKGO:
    from lms.djangoapps.instructor_task.tasks_base import BaseInstructorTask
    from lms.djangoapps.instructor_task.tasks_helper.runner import run_main_task, TaskProgress
    from lms.djangoapps.instructor_task.tasks_helper.utils import upload_csv_to_report_store
    from .ginkgo import upload_user_grades_csv
else:
    from lms.djangoapps.instructor_task.tasks_helper import BaseInstructorTask
    from lms.djangoapps.instructor_task.tasks_helper import run_main_task, upload_csv_to_report_store
    from lms.djangoapps.instructor_task.tasks_helper import TaskProgress
    from .ficus import upload_user_grades_csv