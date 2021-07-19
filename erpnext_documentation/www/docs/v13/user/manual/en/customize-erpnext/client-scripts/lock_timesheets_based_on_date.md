<!-- add-breadcrumbs -->
# Lock Time Sheets Based on Date

Let's say you would like all employees to fill time sheets by Friday of every week. And allow only those users having 'Projects Manager' role to edit or add time sheets for days prior to the latest Friday. Below custom script will implement this feature.

    frappe.ui.form.on("Timesheet", "validate", function(frm) {
        if (frappe.user_roles.indexOf("Projects Manager") == -1) {
            const t = new Date().getDate() + (6 - new Date().getDay() - 1) - 7;
            const lastFriday = new Date();
            lastFriday.setDate(t);

            let dd = lastFriday.getDate();
            let mm = lastFriday.getMonth() + 1;
            let yyyy = lastFriday.getFullYear();

            frm.doc.time_logs.forEach(log => {
                if (new Date(log.from_time) <= lastFriday) {
                    frappe.throw("You cannot add timesheet for dates before last Friday " + dd + "/" + mm + "/" + yyyy + ". Please contact your Project Manager.");
                }
            })
        }
    })

{next}
