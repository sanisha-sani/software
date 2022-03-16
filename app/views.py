from django.shortcuts import render

# Create your views here.


#***********************developer***********************************************
def index(request):
    return render(request,'index.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    
def pm_Dashboard(request):
    return render(request, 'pm\pm_Dashboard.html')

def pm_projects(request):
    return render(request, 'pm\pm_projects.html')

def pm_upcomingProject(request):
    return render(request, 'pm\pm_upcomingProject.html')

def pm_currentProject(request):
    return render(request, 'pm\pm_currentProject.html')

def pm_completedProject(request):
    return render(request, 'pm\pm_completedProject.html')

def pm_createProject(request):
    return render(request, 'pm\pm_createProject.html')

def pm_newProj_status(request):
    return render(request, 'pm\pm_newProj_status.html')


def pm_assignProject(request):
    return render(request, 'pm\pm_assignProject.html')

def pm_newProject(request):
    return render(request, 'pm\pm_newProject.html')

def pm_acceptedProject(request):
    return render(request, 'pm\pm_acceptedProject.html')

def pm_rejectedProject(request):
    return render(request, 'pm\pm_rejectedProject.html')

def pm_currentProjectFirst(request):
    return render(request, 'pm\pm_currentProjectFirst.html')

def pm_currentprojectTeam(request):
    return render(request, 'pm\pm_currentprojectTeam.html')

def pm_currentprojectTeamList(request):
    return render(request, 'pm\pm_currentprojectTeamList.html')

def pm_completedFirst(request):
    return render(request, 'pm\pm_completedFirst.html')

def pm_completeProj_Team(request):
    return render(request, 'pm\pm_completeProj_Team.html')

def pm_completeProj_Teamlist(request):
    return render(request, 'pm\pm_completeProj_Teamlist.html')

def pm_employee(request):
    return render(request, 'pm\pm_employee.html')

def pm_employee_TL(request):
    return render(request, 'pm\pm_employee_TL.html')

def pm_TL_Team(request):
    return render(request, 'pm\pm_TL_Team.html')

def pm_TL_Team_profile(request):
    return render(request, 'pm\pm_TL_Team_profile.html')

def pm_TL_Team_involved(request):
    return render(request, 'pm\pm_TL_Team_involved.html')

def pm_TL_Team_attendence(request):
    return render(request, 'pm\pm_TL_Team_attendence.html')

def pm_TL_Team_viewAttendence(request):
    return render(request, 'pm\pm_TL_Team_viewAttendence.html')

def pm_employee_developer(request):
    return render(request, 'pm\pm_employee_developer.html')

def pm_emp_developers_dashboard(request):
    return render(request, 'pm\pm_emp_developers_dashboard.html')

def pm_developer_team(request):
    return render(request, 'pm\pm_developer_team.html')

def pm_tl_dashboard(request):
    return render(request, 'pm\pm_tl_dashboard.html')

def pm_reportedIssues(request):
    return render(request, 'pm\pm_reportedIssues.html')

def pm_report_reportedIssue(request):
    return render(request, 'pm\pm_report_reportedIssue.html')

def pm_reportedIssue_action(request):
    return render(request, 'pm\pm_reportedIssue_action.html')

def pm_report_issue(request):
    return render(request, 'pm\pm_report_issue.html')

def pm_tl_reported_issues(request):
    return render(request, 'pm\pm_tl_reported_issues.html')

def pm_tl_issuesVerified(request):
    return render(request, 'pm\pm_tl_issuesVerified.html')

def pm_applyLeave(request):
    return render(request, 'pm\pm_applyLeave.html')

def pm_applyleave_Form(request):
    return render(request, 'pm\pm_applyleave_Form.html')

def pm_requested_leave(request):
    return render(request, 'pm\pm_requested_leave.html')

def pm_Attendence(request):
    return render(request, 'pm\pm_Attendence.html')

def pm_attendenceList(request):
    return render(request, 'pm\pm_attendenceList.html')

def pm_TL_attendence(request):
    return render(request, 'pm\pm_TL_attendence.html')

def pm_TL_attendencelist(request):
    return render(request, 'pm\pm_TL_attendencelist.html')

def pm_developer_attendence(request):
    return render(request, 'pm\pm_developer_attendence.html')

def pm_developer_attendencelist(request):
    return render(request, 'pm\pm_developer_attendencelist.html')