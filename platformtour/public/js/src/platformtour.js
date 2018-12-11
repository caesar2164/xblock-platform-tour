function PlatformTourXBlock(runtime, element) {
    $('button.navmaker', element).click(function(){
        introJs().start();
    });
}
