//var myHeading = document.querySelector('h1');
//myHeading.textContent = 'Hi from JS world!';

var app1 = new Vue({
  el: '#app-cell-1',
  data: {
    message: '%!'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})


var app2 = new Vue({
  el: '#app-cell-2',
  data: {
    message: '!?'
  },
  methods: {
    reverseMessage: function () {
      this.message = this.message.split('').reverse().join('')
    }
  }
})
