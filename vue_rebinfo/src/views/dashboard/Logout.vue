<!-- update the logout link as below -->
<a class="item" @click="logout">
    <i class="sign out icon"></i>
</a>

// add these to `methods`


<script>

export default {
    name: 'Logout',
    methods: {
       logout () {
    localStorage.removeItem('token')

    this.$router.push('/')
}
</script>