<template>
    <div class="page-signup">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Sign up</h1>
            </div>

            <div class="column is-6">
              <div class="field">
                        <label>E-mail</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="user.email">
                        </div>
                    </div>
                     <div class="field">
                        <label>Username</label>
                        <div class="control">
                            <input type="text" name="username" class="input" v-model="user.username">
                        </div>
                    </div>

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password" class="input" v-model="user.password">
                        </div>
                    </div>
                <div class="field">
                        <label>Management</label>
                        <div class="control">
                            <input type="text" name="is_management" class="input" v-model="user.is_management">
                        </div>
                    </div>
                    </div>

            <div class="column is-12">
                <div class="field">
                    <div class="control">
                        <button class="button is-success" @click="submitForm">Submit</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'SignUp',
   data () {
        return {
            user: {
                  email: '',
                  username: '',
				  password: '',
				  is_management: ''
            }
        }
    },
    methods: {
        submitForm() {
          {
            this.user.email = this.user.email,
            this.user.username = this.user.username,
            this.user.password = this.user.password,
            this.user.is_management = this.user.is_management
            }
            axios
                .post("/api/v1/register/", this.user)
                .then(response => {
                    toast({
                        message: 'The User was added',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push('/log-in')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>