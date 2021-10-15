<template>
  <div id="app">
        <div>
                    <nav class="navbar navbar-expand navbar-dark bg-dark">
                      <a href class="navbar-brand" @click.prevent>BREB PBS</a>
                      <div class="navbar-nav mr-auto">
                        <li class="nav-item">
                          <router-link to="/home" class="nav-link">
                            <font-awesome-icon icon="home" />Home
                          </router-link>
                        </li>


                         <li v-if="showAdminBoard" class="nav-item">
                          <router-link to="/admin" class="nav-link">Admin Board</router-link>
                        </li>
                        <li v-if="showModeratorBoard" class="nav-item">
                          <router-link to="/mod" class="nav-link">Moderator Board</router-link>
                        </li>
                        <li class="nav-item">
                          <router-link v-if="currentUser" to="/user" class="nav-link">User</router-link>
                        </li>
                      </div>

                      <div v-if="!currentUser" class="navbar-nav ml-auto">
                        <li class="nav-item">
                          <router-link to="/register" class="nav-link">
                            <font-awesome-icon icon="user-plus" />Sign Up
                          </router-link>
                        </li>
                        <li class="nav-item">
                          <router-link to="/login" class="nav-link">
                            <font-awesome-icon icon="sign-in-alt" />Login
                          </router-link>
                        </li>
                      </div>

                      <div v-if="currentUser" class="navbar-nav ml-auto">
                        <li class="nav-item">
                          <router-link to="/profile" class="nav-link">
                            <font-awesome-icon icon="user" />
                            {{ currentUser.username }}
                          </router-link>
                        </li>
                        <li class="nav-item">
                          <a class="nav-link" href @click.prevent="logOut">
                            <font-awesome-icon icon="sign-out-alt" />LogOut
                          </a>
                        </li>
                      </div>
                    </nav>


        </div>




            <div>

<nav class="w3-sidebar w3-collapse w3-white w3-animate-left" style="z-index:3;width:300px;" id="mySidebar"><br>
                      <div v-if="currentUser" class="w3-bar-block">
                        <i class="fas fa-trash-alt"></i>
                        <router-link to="/home" class="w3-bar-item w3-button w3-padding w3-blue"><i class="fa fa-users fa-fw"></i>Home</router-link>
                       <router-link v-if="showUserBoard"  to="/addnetmeter" class="w3-bar-item w3-button w3-padding"><i class="fa fa-eye fa-fw"></i>addNetmeter</router-link>
                       <router-link v-if="showAdminBoard" to="/netmeterlist" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bank fa-fw"></i>NetmeterEdit</router-link>
                        <router-link to="/netmeterrpt" class="w3-bar-item w3-button w3-padding"><i class="fa fa-history fa-fw"></i>Netmeter Report</router-link>
                        <router-link v-if="showUserBoard" to="/addsolar" class="w3-bar-item w3-button w3-padding"><i class="fa fa-eye fa-fw"></i>addSolar</router-link>
                       <router-link v-if="showAdminBoard" to="/netmeterlist" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bank fa-fw"></i>SolarEdit</router-link>
                        <router-link to="/solarrpt" class="w3-bar-item w3-button w3-padding"><i class="fa fa-history fa-fw"></i>Solar Report</router-link>
                        <router-link v-if="showUserBoard" to="/addchargestation" class="w3-bar-item w3-button w3-padding"><i class="fa fa-eye fa-fw"></i>addChargingStation</router-link>
                       <router-link v-if="showAdminBoard" to="/netmeterlist" class="w3-bar-item w3-button w3-padding"><i class="fa fa-bank fa-fw"></i>ChargingStationEdit</router-link>
                        <router-link to="/cstationrpt" class="w3-bar-item w3-button w3-padding"><i class="fa fa-history fa-fw"></i>ChargingStation Report</router-link>
                        <router-link to="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-diamond fa-fw"></i> Logout</router-link>
                          <router-link to="#" class="w3-bar-item w3-button w3-padding"><i class="fa fa-cog fa-fw"></i> Settings</router-link><br><br>

                      </div>
                    </nav>


            </div>



                      <div>


                    <div class="container">
                      <router-view />
                    </div>




            </div>






  </div>
</template>

<script>
export default {
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
    showAdminBoard() {
      if (this.currentUser && this.currentUser.user_role) {
        return this.currentUser.user_role.includes('admin');
      }
      return false;
    },
    showUserBoard() {
      if (this.currentUser && this.currentUser.user_role) {
        return this.currentUser.user_role.includes('user');
      }
      return false;
    },
    showModeratorBoard() {
      if (this.currentUser && this.currentUser.roles) {
        return this.currentUser.roles.includes('ROLE_MODERATOR');
      }
      return false;
    }
  },
  methods: {
    logOut() {
      this.$store.dispatch('auth/logout');
      this.$router.push('/login');
    }
  }
};

</script>