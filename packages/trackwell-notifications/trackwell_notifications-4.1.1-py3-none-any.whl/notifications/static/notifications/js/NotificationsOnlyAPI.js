var WAIT_UNTIL_NEXT_NOTIFICATION_MS = 800;

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function NotificationClient() {
  this.cookieName = 'notifications';
  this.request = null;
  this.options = {};
  this.modalContainer = null;
  this.overlay = null;
  this.notification = null;
  this.notifications = [];
}

NotificationClient.prototype = {
  setModalContainer: function (modalContainer) {
    this.modalContainer = document.body.appendChild(modalContainer);
  },
  showModal: function (notification) {
    if (!notification) return;
    var that = this;

    var modalContainer = document.createElement('div');
    if (notification === null || notification === undefined || notification.notification === undefined) {
      // Malformed response, out of synch cache or the like
      return;
    }

    modalContainer.className = 'notification notification-' + notification.notification.look;

    if (notification.notification.look === 'RELEASE_NOTES') {
      var isActive = false;

      var iconButton = document.createElement('button');
      iconButton.className = 'notification-RELEASE_NOTES-button';

      var bellIcon = document.createElement('i');
      bellIcon.className = 'notifications-font-bell';
      bellIcon.style.cssText = "font-size: 16px; color: #ff4a3f;";

      iconButton.appendChild(bellIcon);
      iconButton.onclick = function () {
        if (isActive) {
          this.iconButton = document.body.removeChild(iconButton);
          that.dismissNotification(true, 'OK');
        } else {
          that.setModalContainer(modalContainer);
        }
        isActive = !isActive;
      }

      var titleContainer = document.createElement('div');
      titleContainer.className = 'titleContainer';

      var exitButton = document.createElement('button');
      exitButton.className = 'notification-exit-button'
      exitButton.onclick = function () {
        this.iconButton = document.body.removeChild(iconButton);
        that.dismissNotification(true, 'OK');
        isActive = !isActive;
      };
      exitIcon = document.createElement('i');
      exitIcon.className = 'notifications-font-times';
      exitIcon.style.cssText = "font-size: 24px; color: #636363;";
      exitButton.appendChild(exitIcon);

      var title = document.createElement('h1');
      title.innerHTML = notification.notification.name;
      titleContainer.appendChild(exitButton);
      titleContainer.appendChild(title);
      modalContainer.appendChild(titleContainer);


      var body = document.createElement('div');
      body.className = 'notification-body';
      body.innerHTML = notification.notification.message;
      modalContainer.appendChild(body);

      var snoozeButton = document.createElement('button');
      snoozeButton.innerHTML = gettext('View later');
      snoozeButton.className = 'outline-button';
      snoozeButton.onclick = function () {
        this.iconButton = document.body.removeChild(iconButton);
        that.dismissNotification();
        isActive = !isActive;
      };
      modalContainer.appendChild(snoozeButton);

      var overlay = document.createElement('div');
      overlay.className = 'notification-overlay';

      this.iconButton = document.body.appendChild(iconButton);


    } else {
      if (notification.notification.look === 'SIMPLE_OK') {
        var titleContainer = document.createElement('div');
        titleContainer.className = 'titleContainer';

        var exitButton = document.createElement('button');
        exitButton.onclick = function () {
          that.dismissNotification(true, 'OK');
        };
        exitIcon = document.createElement('i');
        exitIcon.className = 'notifications-font-times';
        exitIcon.style.cssText = "font-size: 24px; color: #636363;";
        exitButton.appendChild(exitIcon);

        var title = document.createElement('h1');
        title.innerHTML = notification.notification.name;
        titleContainer.appendChild(exitButton);
        titleContainer.appendChild(title);
        modalContainer.appendChild(titleContainer);
      }

      if (notification.notification.image !== null) {
        var imageContainer = document.createElement('img');
        imageContainer.src = notification.notification.image;
        imageContainer.alt = 'Notification image';
        imageContainer.className = 'notification-image';
        modalContainer.appendChild(imageContainer);
      }

      var body = document.createElement('div');
      body.className = 'notification-body';
      body.innerHTML = notification.notification.message;
      modalContainer.appendChild(body);

      var overlay = document.createElement('div');
      overlay.className = 'notification-overlay';


      if (notification.notification.look === 'SIMPLE_OK') {
        var buttonContainer = document.createElement('div');
        buttonContainer.className = 'notification-form-buttons';
        modalContainer.appendChild(buttonContainer);

        var approveButton = document.createElement('button');
        var approveText = that.notifications.length > 1 ? gettext('Next') : gettext('Ok');
        approveButton.innerHTML = approveText;
        approveButton.onclick = function () {
          that.dismissNotification(true, 'OK');
        };
        buttonContainer.appendChild(approveButton);

        var snoozeButton = document.createElement('button');
        snoozeButton.innerHTML = gettext('View later');
        snoozeButton.className = 'outline-button';
        snoozeButton.onclick = function () {
          that.dismissNotification();
        };
        buttonContainer.appendChild(snoozeButton);

      }

      if (notification.notification.look === 'SIGN_COMPANY') {
        var formContainer = document.createElement('div');
        formContainer.className = 'notification-form';
        modalContainer.appendChild(formContainer);

        var buttonContainer = document.createElement('div');
        buttonContainer.className = 'notification-form-buttons';
        modalContainer.appendChild(buttonContainer);

        var inputField = document.createElement('input');
        inputField.placeholder = gettext('Company name ');
        var snoozeButton = document.createElement('button');
        snoozeButton.innerHTML = gettext('Not now');
        var approveButton = document.createElement('button');
        approveButton.innerHTML = gettext('Approve');

        snoozeButton.onclick = function () {
          that.dismissNotification(false, inputField.value);
        };
        approveButton.onclick = function () {
          that.dismissNotification(true, inputField.value);
        };
        formContainer.appendChild(inputField);
        formContainer.appendChild(buttonContainer);
        buttonContainer.appendChild(snoozeButton);
        buttonContainer.appendChild(approveButton);
      }
      that.setModalContainer(modalContainer);
      this.overlay = document.body.appendChild(overlay);

      if (document.body.offsetWidth < 600) {
        modalContainer.style.left = '0';
      } else {
        modalContainer.style.marginLeft = -this.modalContainer.offsetWidth / 2 + 'px';
      }
    }
  },
  closeModal: function () {
    this.modalContainer.parentNode.removeChild(this.modalContainer);
    if (this.overlay) {
      this.overlay.parentNode.removeChild(this.overlay);
    }
    this.modalContainer = null;
    this.overlay = null;
    this.notifications.shift();
    if (this.notifications.length > 0) {
      this.notification = this.notifications[0];
    } else {
      this.notification = null;
    }
  },
  setupRequest: function (onSuccess) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function () {
      if (request.readyState === 4) {
        if (request.status === 200) {
          onSuccess(request);
        } else {
          console.log('An error occurred during your request: ' + request.status + ' ' + request.statusText);
        }
      }
    };
    return request;
  },
  dismissNotification: function (answer, answer_string) {
    var that = this;
    var APIUrl = window.notificationEndpoint || '/api2/usernotifications/';  // Default in timon
    var request = this.setupRequest(function (request) {
      that.closeModal();
      setTimeout(function () {
        if (typeof that.notification !== 'undefined' || that.notification !== null) {
          that.showModal(that.notification);
        }
      }, WAIT_UNTIL_NEXT_NOTIFICATION_MS);
    });
    request.open('PATCH', APIUrl + this.notification.id + '/');
    request.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    request.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
    request.send(JSON.stringify({
      answer: answer,
      answer_string: answer_string
    }));
  },
  checkAndShow: function () {
    var that = this;
    var request = this.setupRequest(function (request) {
      that.notifications = JSON.parse(request.responseText);
      if (that.notifications.length > 0) {
        that.notification = that.notifications[0];
        that.showModal(that.notification);
      }
    });
    var path = window.location.pathname;
    var APIUrl = window.notificationEndpoint || '/api2/usernotifications/';  // Default in timon
    request.open('GET', APIUrl + '?path=' + path);
    request.send();
  }
};

function ready(callbackFunc) {
  if (document.readyState !== 'loading') {
    // Document is already ready, call the callback directly
    callbackFunc();
  } else if (document.addEventListener) {
    // All modern browsers to register DOMContentLoaded
    document.addEventListener('DOMContentLoaded', callbackFunc);
  } else {
    // Old IE browsers
    document.attachEvent('onreadystatechange', function () {
      if (document.readyState === 'complete') {
        callbackFunc();
      }
    });
  }
}

ready(function () {
  var nc = new NotificationClient();
  nc.typeInName = true;
  nc.checkAndShow();
});
