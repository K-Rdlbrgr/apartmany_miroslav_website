$('.cards').click(function() {
  $(this).toggleClass('flip');
});

function toggleText1() {
  var text = document.getElementById('header-switch1');
  var sign = document.getElementById('header-switch1-i');
  if (text.style.display === 'none') {
    text.style.display = 'block';
  } else {
    text.style.display = 'none';
  }
  if (sign.style.display === 'none') {
    sign.style.display = 'block';
  } else {
    sign.style.display = 'none';
  }
}

function toggleText2() {
  var text = document.getElementById('header-switch2');
  var sign = document.getElementById('header-switch2-i');
  if (text.style.display === 'none') {
    text.style.display = 'block';
  } else {
    text.style.display = 'none';
  }
  if (sign.style.display === 'none') {
    sign.style.display = 'block';
  } else {
    sign.style.display = 'none';
  }
}

// APARTMENT SECTION

$(document).ready(function() {
  var content = $('.content');
  var currentItem = content.filter('.active');
  var steps = $('.card').filter('.steps');
  var inactive1 = $('.inactive-1');
  var inactive2 = $('.inactive-2');
  var inactive3 = $('.inactive-3');
  var inactive4 = $('.inactive-4');
  var inactive5 = $('.inactive-5');
  var inactive6 = $('.inactive-6');
  var inactive7 = $('.inactive-7');
  var inactive8 = $('.inactive-8');
  var inactive9 = $('.inactive-9');

  $('.button').click(function() {
    var nextItem = currentItem.next();
    var lastItem = content.last();
    var contentFirst = content.first();

    currentItem.removeClass('active');

    if (currentItem.is(lastItem)) {
      currentItem = contentFirst.addClass('active');
      currentItem.css({ right: '10%', opacity: '1' });
      $('.step').animate({ width: '10%' });
      inactive1.animate({ height: '8px', marginLeft: '45px', marginRight: '45px', marginBottom: '-10px' }, 100);
      inactive2.animate({ height: '8px', marginLeft: '40px', marginRight: '40px', marginBottom: '-8px' }, 100);
      inactive3.animate({ height: '8px', marginLeft: '35px', marginRight: '35px', marginBottom: '-6px' }, 100);
      inactive4.animate({ height: '8px', marginLeft: '30px', marginRight: '30px', marginBottom: '-4px' }, 100);
      inactive5.animate({ height: '8px', marginLeft: '25px', marginRight: '25px', marginBottom: '-2px' }, 100);
      inactive6.animate({ height: '8px', marginLeft: '20px', marginRight: '20px', marginBottom: '0px' }, 100);
      inactive7.animate({ height: '8px', marginLeft: '15px', marginRight: '15px', marginBottom: '0px' }, 100);
      inactive8.animate({ height: '8px', marginLeft: '10px', marginRight: '10px', marginBottom: '0px' }, 100);
      inactive9.animate({ height: '8px', marginLeft: '5px', marginRight: '5px', marginBottom: '0px' }, 100);
      var in5 = document.getElementById('inactive-5');
      var in4 = document.getElementById('inactive-4');
      var in3 = document.getElementById('inactive-3');
      var in2 = document.getElementById('inactive-2');
      var in1 = document.getElementById('inactive-1');
      in5.style.display = 'none';
      in4.style.display = 'none';
      in3.style.display = 'none';
      in2.style.display = 'none';
      in1.style.display = 'none';
    } else if (currentItem.is(contentFirst)) {
      var in5 = document.getElementById('inactive-5');
      currentItem.animate({ opacity: 0 }, 1000);
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '20%' });
      inactive9.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
      in5.style.display = 'block';
    } else if (currentItem.is(':nth-child(2)')) {
      var in4 = document.getElementById('inactive-4');
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '30%' });
      inactive8.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
      in4.style.display = 'block';
    } else if (currentItem.is(':nth-child(3)')) {
      var in3 = document.getElementById('inactive-3');
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '40%' });
      inactive7.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
      in3.style.display = 'block';
    } else if (currentItem.is(':nth-child(4)')) {
      var in2 = document.getElementById('inactive-2');
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '50%' });
      inactive6.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
      in2.style.display = 'block';
    } else if (currentItem.is(':nth-child(5)')) {
      var in1 = document.getElementById('inactive-1');
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '60%' });
      inactive5.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
      in1.style.display = 'block';
    } else if (currentItem.is(':nth-child(6)')) {
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '70%' });
      inactive4.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
    } else if (currentItem.is(':nth-child(7)')) {
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '80%' });
      inactive3.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
    } else if (currentItem.is(':nth-child(8)')) {
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '90%' });
      inactive2.animate({ height: '0', marginLeft: '5px', marginRight: '5px', marginBottom: '-2px' }, 100);
    } else if (currentItem.is(':nth-child(9)')) {
      currentItem = nextItem.addClass('active');
      $('.step').animate({ width: '100%' });
      inactive1.animate({ height: '6px', marginLeft: '2px', marginRight: '2px' }, 100);
    }
  });
});
