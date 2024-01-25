function submitForm() {
    var message = document.getElementById("message").value;
//    message = "HELLO";
    var email_address = "aditya.neeraje@gmail.com";
    var subject = document.getElementById("subject").value;
    if (subject.length == 0){
        subject="Feedback regarding Portfolio Website";
    }

    if (message.length > 0){
        var mailtoLink = 'mailto:' + email_address + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(message);
        window.open(mailtoLink, '_blank');
    }
    event.preventDefault();
}

function check_state_name() {
    var message = document.querySelector(".state_input").value;
    var data = { "message": message };

    fetch('/check_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}

function display_guessed_state(state_input, give_up=false) {
    var state_label = document.getElementById(state_input);
    state_label.style.display = "block";
    if (give_up) {
        state_label.style.color = "red";
    }
}


function give_hint() {
    var data = { "message": "Hint" };

    fetch('/check_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}

function give_up() {
    var data = { "message": "Give Up" };

    fetch('/check_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}

function restart(){
    var data = {"message": "Restart"};
        fetch('/check_state', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}

function play_othello(number) {
    var elements = document.getElementsByClassName("loc_button");
    for (var i = 0; i < 64; i++){
        elements[i].disabled = true;
    }
    var string = "black_" + number.toString();
    document.getElementById(string).style.display = "block";
    var data = { "message": number };

    fetch('/clicked_button', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}

function display_box(id_name) {
        var element = document.getElementById(id_name);
        element.style.display = "block";
}

function submit_on_pressing_enter() {
    var inputElement = document.getElementsByClassName("state_input")[0];
    var states = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida',
          'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
          'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska',
          'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio',
          'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas',
          'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']

    inputElement.focus();
    inputElement.addEventListener("keyup", function(event) {
        var inputValue = inputElement.value.trim().toLowerCase(); // Use value property to get the input text

        if (states.includes(inputValue)) {
            check_state_name();
        }
        if (event.key === "Enter") {
            check_state_name();
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    var txt = document.getElementsByClassName("title")[0].innerText; // Use getElementsByClassName and access the first element
    var speed = 50;
    var i = 0;
    document.getElementsByClassName("title")[0].innerText = "";

    function typeWriter() {
        if (i < txt.length) {
            document.getElementsByClassName("title")[0].innerHTML += txt.charAt(i);
            i++;
            setTimeout(typeWriter, speed);
        }
    }

    typeWriter();
});

document.addEventListener("DOMContentLoaded", function () {
  var dropdown = document.getElementsByClassName("dropdown")[0];
  var dropdown_menu = document.getElementsByClassName("dropdown-menu")[0];
  var isMouseOnDropdown = false;
  var isMouseOnDropdownMenu = false;

  dropdown.addEventListener("mouseenter", function () {
    isMouseOnDropdown = true;
    dropdown_menu.style.display="block";
  });

  dropdown.addEventListener("mouseleave", function () {
    isMouseOnDropdown = false;
    setTimeout(function () {
      if (!isMouseOnDropdown && !isMouseOnDropdownMenu)
        dropdown_menu.style.display = "none";
    }, 1000);
  });

  dropdown_menu.addEventListener("mouseenter", function () {
    isMouseOnDropdownMenu = true;
    dropdown_menu.style.display="block";
  });

  dropdown_menu.addEventListener("mouseleave", function () {
    isMouseOnDropdownMenu = false;
    setTimeout(function () {
      if (!isMouseOnDropdownMenu && !isMouseOnDropdown)
        dropdown_menu.style.display = "none";
    }, 1000);
  });
});
document.addEventListener("DOMContentLoaded", function () {
  var dropdown = document.getElementsByClassName("dropdown")[0];
  var dropdown_menu = document.getElementsByClassName("dropdown-menu")[0];
  var isMouseOnDropdown = false;
  var isMouseOnDropdownMenu = false;
  var timeoutId;

  function hideDropdownMenu() {
    timeoutId = setTimeout(function () {
      if (!isMouseOnDropdown && !isMouseOnDropdownMenu) {
        dropdown_menu.style.display = "none";
      }
    }, 1000);
  }

  dropdown.addEventListener("mouseenter", function () {
    isMouseOnDropdown = true;
    clearTimeout(timeoutId);
  });

  dropdown.addEventListener("mouseleave", function () {
    isMouseOnDropdown = false;
    hideDropdownMenu();
  });

  dropdown_menu.addEventListener("mouseenter", function () {
    isMouseOnDropdownMenu = true;
    clearTimeout(timeoutId);
  });

  dropdown_menu.addEventListener("mouseleave", function () {
    isMouseOnDropdownMenu = false;
    hideDropdownMenu();
  });
});

function restart_othello() {
    var data = { "message": "Restart" };

    fetch('/restart_othello', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        window.location.href = data.redirect_path;
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Some error has occurred.')
    });
}