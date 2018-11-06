function PlatformTourXBlock(runtime, element) {
    var stepList = JSON.parse($('.navmaker-steps', element).text());
    var platformTourData = [];
    var stepsAdded = 1;
    stepList.forEach(function(step, i) {
        var stepElement = $(step.selector);
        if (step.find) {
            stepElement = $(step.selector).find(step.find);
        }
        if (stepElement) {
            platformTourData.push(stepElement);
            platformTourData[i].attr('data-step', stepsAdded);
            platformTourData[i].attr('data-intro', step.dataIntro);
            platformTourData[i].attr('data-position', step.dataPosition);
            var screenReaderListItem = '<li class="step">' + step.dataIntro + '</li>';
            $('.screen-reader-steps', element).append(screenReaderListItem);
            stepsAdded++;
        }
    });

    $('button.navmaker', element).click(function(){
        introJs().start();
    });
}
