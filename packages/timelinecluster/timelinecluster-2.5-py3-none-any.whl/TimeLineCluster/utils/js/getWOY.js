function getWeekOfYear(time) {
    var weekFlag = 0
    var currentDate = new Date(time);
    currentDate.setHours(0);
    currentDate.setMinutes(0);
    currentDate.setSeconds(0);
    currentDate.setMilliseconds(0);
    while (true){
        var weekOfYear;
        var addDateToSat = (7 - currentDate.getDay()) * 24 * 60 * 60 * 1000;
        var date = new Date((currentDate.getTime() + addDateToSat));
        var newYear = new Date(date.getTime());
        newYear.setDate(1);
        newYear.setMonth(0);
        newYear.setHours(0);
        newYear.setMinutes(0);
        newYear.setSeconds(0);
        newYear.setMilliseconds(0);
        var firstWeekDate;

        if (newYear.getDay() === 0) {
            firstWeekDate = new Date(newYear.getTime());
        } else {
            var addTime = (7 - newYear.getDay()) * 24 * 60 * 60 * 1000;
            firstWeekDate = new Date( (newYear.getTime() + addTime) )
        }
        var diffTime = date.getTime() - firstWeekDate.getTime();
        var diffWeek = Math.round(diffTime / (7 * 24 * 60 * 60 * 1000));
        if(diffWeek === 0){
            currentDate.setDate(currentDate.getDate() - 1);
            weekFlag = 1
            continue;
        }
        weekOfYear = {
            week: diffWeek + weekFlag,
            year: currentDate.getFullYear()
        };
        return weekOfYear;
    }
}