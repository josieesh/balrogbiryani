<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <Word :numLetters="5"/>
  </div>
</template>

<script>
import Word from './components/Word.vue'

export default {
  name: 'App',
  components: {
    Word
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
