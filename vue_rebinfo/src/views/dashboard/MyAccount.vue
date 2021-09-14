<template>
    <div class="page-my-account">
        <h1 class="title">My account</h1>

        <button @click="logout()" class="button is-danger">Log out</button>
    </div>
</template>

<script>


export default {
    name: 'MyAccount',
    methods: {
       logout () {
        localStorage.removeItem('token')
        this.$router.push('/log-in')
      }
      }
      }
</script>