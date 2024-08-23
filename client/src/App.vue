<template>
<div class="main-cont">
  <div>
    <h1>Welcome Penny Pincher</h1>
  </div>
  <div class="dark-div">
    <ExpenseForm />
  </div>
</div>
</template>

<script>
import ExpenseForm from './components/ExpenseForm.vue'

export default {
  name: 'App',
  components: {
    ExpenseForm
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  margin-top: 60px;
}

.main-cont {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.dark-div {
  border: 1px solid black;
  border-radius: 4px;
}
</style>
