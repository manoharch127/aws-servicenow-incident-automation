(function process(request, response) {

var data = request.body.data;

var inc = new GlideRecord('incident');
inc.initialize();

inc.short_description = "AWS Alert: " + data.AlarmName;
inc.description = JSON.stringify(data);

if(data.State == "ALARM"){
    inc.priority = 1;
} else {
    inc.priority = 3;
}

inc.assignment_group = "Cloud Support";

var sysId = inc.insert();

response.setStatus(200);

response.setBody({
    message: "Incident Created",
    sys_id: sysId
});

})(request, response);
