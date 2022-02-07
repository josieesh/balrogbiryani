<template>
  <div class="word">
    <form @submit.prevent="submit" id="form">
        <label for="name">{{ numLetters }} letters</label>
        <br>
        <input type="text" id="guess" v-model="guess" required
            v-bind:minlength="numLetters" v-bind:maxlength="numLetters" size="14"
             v-on:input="clear">
    </form>
  </div>
</template>

<script>
// var numLetters = this.word.length()
// document.getElementById("guess").innerHTML = "".concat(numLetters, " letters") 
// document.getElementById("guess").setAttribute("minLength", numLetters);
// document.getElementById("guess").setAttribute("maxLength", numLetters);
export default {
  name: 'Word',
  props: {
    word: String
  },
  methods : {
    submit : function(){
        if (this.guess == this.word) {
            console.log("correct!");
            document.getElementById("guess").className = "correct";
        } else {
            document.getElementById("guess").className = "wrong";
        }
    },
    clear: function() {
        document.getElementById("guess").className = "";
    }
  },
  data() {
      return {
        numLetters: 0,
        guess: ""
      }
  },
  created() {
      this.numLetters = this.word.length;
  },
  afterMount(){
    const guess = document.getElementById("guess");
    guess.addEventListener("keyup", function(event) {
        event.preventDefault();
        if (event.keyCode === 13) {
            document.getElementById("form").submit();
        }
    });
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input.wrong, textarea { 
    background: red; 
}
input.correct, textarea { 
    background: cyan;
}
input {
text-align: center;
background: white;
}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
