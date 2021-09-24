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

      <div class="form-group">
        <label for="month">month</label>
        <input
          type="text"
          class="form-control"
          id="month"
          required
          v-model="netmeterinfo.month"
          name="month"
        />
      </div>
      <div class="form-group">
        <label for="year">year</label>
        <input
          type="text"
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
      <div class="form-group">
        <label for="pbs_code">office_code</label>
        <input
          type="text"
          class="form-control"
          id="pbs_code"
          required
          v-model="netmeterinfo.pbs_code"
          name="pbs_code"
        />
      </div>

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
        pbs_code: this.netmeterinfo.pbs_code
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