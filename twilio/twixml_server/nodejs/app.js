
var accountSid = 'b0';
var authToken = "22480ef";
var client = require('twilio')(accountSid, authToken);

client.calls.create({
    url: "http://b7643413.ngrok.io/make_call",
    to: "+14163128887",
    from: "+14163128234"
}, function(err, call) {
    process.stdout.write(call.sid);
});
