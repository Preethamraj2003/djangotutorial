document.addEventListener('DOMContentLoaded', function () {
    var employeeDropdown = document.getElementById('employeeselect');
    var designationDropdown = document.getElementById('designation');
    
    if (employeeDropdown) {
        employeeDropdown.addEventListener('change', function() {
            document.getElementById('employeeform').submit();
        });
    }
    
    if (designationDropdown) {
        designationDropdown.addEventListener('change', function() {
            document.getElementById('employeeform').submit();
        });
    }
});