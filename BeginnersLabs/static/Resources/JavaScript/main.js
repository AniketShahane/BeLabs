//ToolTips
const tooltips_elements = document.querySelectorAll('.tooltipped');
M.Tooltip.init(tooltips_elements, {});

//Collapsible Section
const collapses = document.querySelectorAll('.collapsible');
M.Collapsible.init(collapses, {});

//sideNav
const sidenavigation = document.querySelector('.sidenav');
M.Sidenav.init(sidenavigation, {});

//clickable images -- Single Blog Section
const imageboxed = document.querySelectorAll('.materialboxed');
M.Materialbox.init(imageboxed, {
  inDuration: 300,
  outDuration: 300
});

//Modal for creating new messages
const modal_elements = document.querySelectorAll('.modal');
M.Modal.init(modal_elements, {});

// Light Box Options
// lightbox.option({
//   'resizeDuration': 200,
//   'wrapAround': true,
//   'maxHeight': 800,
//   'fadeDuration': 1000
// });


//Scroll Reveal
ScrollReveal().reveal('.head', {
  delay: 400,
  distance: "30px"
});
ScrollReveal().reveal('#main-content', {
  delay: 400,
  distance: "-30px"
});
ScrollReveal().reveal('#main-quote', {
  delay: 400,
  origin: 'left',
  distance: "100px"
});
ScrollReveal().reveal('.nav-wrapper', {
  delay: 400,
  origin: 'top',
  distance: "20px"
});
ScrollReveal().reveal('.card', {
  delay: 400,
  interval: 120,
  origin: 'bottom',
  distance: "80px"
});
ScrollReveal().reveal('.main-collapse', {
  delay: 300,
  interval: 200,
  origin: 'bottom',
  distance: "40px"
});
ScrollReveal().reveal('.blog-header', {
  delay: 400,
  origin: 'top',
  distance: "20px"
});
ScrollReveal().reveal('.search', {
  delay: 400,
  origin: 'top',
  distance: "20px"
});
ScrollReveal().reveal('.message-header', {
  delay: 400,
  distance: "30px",
  origin: 'top'
});
ScrollReveal().reveal('.dashboard-header', {
  delay: 400,
  distance: "15px"
});
ScrollReveal().reveal('.card-small', {
  delay: 400,
  distance: "10px",
  origin: 'bottom'
});
ScrollReveal().reveal('.icon', {
  delay: 400,
  distance: "30px",
  origin: 'top'
});
ScrollReveal().reveal('.img-reveal', {
  delay: 400,
  interval: 100,
  origin: 'bottom',
  distance: "80px",
  mobile: false
});
ScrollReveal().reveal('.blog-icons', {
  delay: 400,
  distance: "40px",
  origin: 'bottom'
});
ScrollReveal().reveal('#chat_person', {
  delay: 400,
  distance: "15px",
  origin: 'top'
});
ScrollReveal().reveal('.comment_text', {
  delay: 400,
  interval: 100,
  origin: 'bottom',
  distance: "80px",
  mobile: false
});
ScrollReveal().reveal('#register-button', {
  delay: 400,
  distance: "15px",
  origin: "top"
});
ScrollReveal().reveal('#login-button', {
  delay: 400,
  distance: "15px",
  origin: "top"
});

$('.count').each(function() {
  $(this).prop('Counter', 0).animate({
    Counter: $(this).text()
  }, {
    duration: 2000,
    easing: 'swing',
    step: function(now) {
      $(this).text(Math.ceil(now));
    }
  });
});

var objDiv = document.querySelector(".person_comments");
objDiv.scrollTop = objDiv.scrollHeight;