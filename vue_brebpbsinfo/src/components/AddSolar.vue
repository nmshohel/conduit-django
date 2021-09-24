<template>
  <div class="submit-form">
    <div v-if="!submitted">
      <div class="form-group">
        <label for="last_month_solar_panel_consumer_nos">last_month_solar_panel_consumer_nos</label>
        <input
          type="text"
          class="form-control"
          id="last_month_solar_panel_consumer_nos"
          required
          v-model="solarpanelinfo.last_month_solar_panel_consumer_nos"
          name="last_month_solar_panel_consumer_nos"
        />
      </div>

      <div class="form-group">
        <label for="last_month_solar_panel_capacity">last_month_solar_panel_capacity</label>
        <input
          type="text"
          class="form-control"
          id="last_month_solar_panel_capacity"
          required
          v-model="solarpanelinfo.last_month_solar_panel_capacity"
          name="last_month_solar_panel_capacity"
        />
      </div>

      <div class="form-group">
        <label for="month">month</label>
        <input
          type="text"
          class="form-control"
          id="month"
          required
          v-model="solarpanelinfo.month"
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
          v-model="solarpanelinfo.year"
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
          v-model="solarpanelinfo.fy"
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
          v-model="solarpanelinfo.pbs_code"
          name="pbs_code"
        />
      </div>

      <button @click="saveTutorial" class="btn btn-success">Submit</button>
    </div>

    <div v-else>
      <h4>You submitted successfully!</h4>
      <button class="btn btn-success" @click="newSolarinfo">Add</button>
    </div>
  </div>
</template>

<script>
import SolarinfoDataService from "../services/solarinfo";

export default {
  name: "add-solarpanelinfo",
  data() {
    return {
      solarpanelinfo: {
        id: null,
        last_month_solar_panel_consumer_nos: "",
        last_month_solar_panel_capacity: "",
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
        last_month_solar_panel_consumer_nos: this.solarpanelinfo.last_month_solar_panel_consumer_nos,
        last_month_solar_panel_capacity: this.solarpanelinfo.last_month_solar_panel_capacity,
        month: this.solarpanelinfo.month,
        year: this.solarpanelinfo.year,
        fy: this.solarpanelinfo.fy,
        pbs_code: this.solarpanelinfo.pbs_code
      };

      SolarinfoDataService.create(data)
        .then(response => {
          this.solarpanelinfo.id = response.data.id;
          console.log(response.data);
          this.submitted = true;
        })
        .catch(e => {
          console.log(e);
        });
    },

    newSolarinfo() {
      this.submitted = false;
      this.solarpanelinfo = {};
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