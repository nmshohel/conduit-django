<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="install_meter_nos">install_meter_nos</label>
        <input
          type="text"
          class="form-control"
          id="install_meter_nos"
          required
          v-model="netmeterinfo.install_meter_nos"
          name="install_meter_nos"
        />
      </div>

      <div class="form-group">
        <label for="capacity_of_install_meter">capacity_of_install_meter</label>
        <input
          type="text"
          class="form-control"
          id="capacity_of_install_meter"
          required
          v-model="netmeterinfo.capacity_of_install_meter"
          name="capacity_of_install_meter"
        />
      </div>
        <label for="month">Month</label>
        <div class="form-group">
             <select class="form-control" v-model="netmeterinfo.month">
             <option disabled value="">Please select month</option>
            <option value="01">January</option>
            <option value="02">February</option>
            <option value="03">March</option>
            <option value="04">April</option>
            <option value="05">May</option>
            <option value="06">June</option>
            <option value="07">July</option>
            <option value="08">August</option>
            <option value="09">September</option>
            <option value="10">October</option>
            <option value="11">November</option>
            <option value="12">December</option>

            </select>
      </div>


      <div class="form-group">
        <label for="year">year</label>
        <input type="number" min="2021" max="2099" step="1" value="2021"
          class="form-control"
          id="year"
          required
          v-model="netmeterinfo.year"
          name="year"
        />
      </div>

      <div class="form-group">
        <label for="fy">fy</label>
        <input
          type="text"
          class="form-control"
          id="fy"
          required
          v-model="netmeterinfo.fy"
          name="fy"
        />
      </div>
      <!-- <label for="pbs_code">pbs_code/label>
        <div class="form-group">
             <select class="form-control" v-model="netmeterinfo.pbs_code">
                        <option value={{currentUser.office_code}}>December</option>

            </select>
      </div> -->
      <div class="form-group">
        <!-- <label for="pbs_code">office_code</label>
        <input
          type="text"
          class="form-control"
          id="pbs_code"
          required
          v-model="netmeterinfo.pbs_code"
          name="pbs_code"
        /> -->

         <!-- v-model=currentUser.office_code -->
      </div>
        {{currentUser.office_code}}
      <button @click="saveTutorial" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newNetmeter">Add</button>
    </div>
  </div>
</template>

<script>
import NetmeterDataService from "../services/netmeter";
 




export default {

  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    }
  },





  name: "add-netmeterinfo",
  data() {
    return {
      netmeterinfo: {
        id: null,
        install_meter_nos: "",
        capacity_of_install_meter: "",
        month: "",
        year: "",
        fy: "",
        pbs_code: "",
        published: false
      },
      submitted: false
    };
  },
  
  methods: {
    saveTutorial() {
      var data = {
        install_meter_nos: this.netmeterinfo.install_meter_nos,
        capacity_of_install_meter: this.netmeterinfo.capacity_of_install_meter,
        month: this.netmeterinfo.month,
        year: this.netmeterinfo.year,
        fy: this.netmeterinfo.fy,
        // pbs_code: this.netmeterinfo.pbs_code
        pbs_code:this.currentUser.office_code
    
      };

      NetmeterDataService.create(data)
        .then(response => {
          this.netmeterinfo.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },
     


    newNetmeter() {
      this.submitted = false;
      this.netmeterinfo = {};
    }
  }
};
</script>

<style>
.submit-form {
  max-width: 300px;
  margin: auto;
}
</style>