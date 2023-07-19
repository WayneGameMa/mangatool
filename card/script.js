$(document).ready(function(){
    $('.card').click(function(arg){
        var set = 'False';
        if ($(this).attr('class') == 'card fertig' && set == 'False'){
            set = 'True'
            $(this).removeClass('fertig');
            $(this).toggleClass('nothing');
        }
        if ($(this).attr('class') == 'card bubble' && set == 'False'){
            set = 'True'
            $(this).removeClass('bubble');
            $(this).toggleClass('fertig');
        }
        if ($(this).attr('class') == 'card raster' && set == 'False'){
            set = 'True'
            $(this).removeClass('raster');
            $(this).toggleClass('bubble');
        }
        if ($(this).attr('class') == 'card ink' && set == 'False'){
            set = 'True'
            $(this).removeClass('ink');
            $(this).toggleClass('raster');
        }
        if ($(this).attr('class') == 'card sketch' && set == 'False'){
            set = 'True'
            $(this).removeClass('sketch');
            $(this).toggleClass('ink');
        }
        if ($(this).attr('class') == 'card story' && set == 'False'){
            set = 'True'
            $(this).removeClass('story');
            $(this).toggleClass('sketch');
        }
        if ($(this).attr('class') == 'card nothing' && set == 'False'){
            set = 'True'
            $(this).removeClass('nothing');
            $(this).toggleClass('story');
        }
        console.log($(this).attr('class'));
    });
});
  