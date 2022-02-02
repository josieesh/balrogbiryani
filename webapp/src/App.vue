<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Word :word="word"/>
  </div>
</template>

<script>
import Word from './components/Word.vue'

//const Http = new XMLHttpRequest();
const url='http://localhost:5000/randomword';

const xmlHttp = new XMLHttpRequest();
xmlHttp.open( "GET", url, false ); // false for synchronous request
xmlHttp.send( null );
var word = xmlHttp.responseText;
console.log(word)

export default {
  name: 'App',
  components: {
    Word
  },
  data() {
   return {
     word: word
   }
 }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
