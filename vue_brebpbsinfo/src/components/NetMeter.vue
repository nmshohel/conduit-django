<template>
  <div v-if="currentTutorial" class="edit-form">
    <h4>Netmeter Information Update</h4>
    <form>
      <div class="form-group">
        <label for="title">pbs_code</label>
        <input type="text" class="form-control" id="pbs_code"
          v-model="currentTutorial.pbs_code"
        />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control" id="install_meter_nos"
          v-model="currentTutorial.install_meter_nos"
        />
      </div>

      <div class="form-group">
        <label><strong>Status:</strong></label>
       <input type="text" class="form-control" id="capacity_of_install_meter"
          v-model="currentTutorial.capacity_of_install_meter"
        />
      </div>
    </form>

    <button class="badge badge-primary mr-2"
      v-if="currentTutorial.published"
      @click="updatePublished(false)"
    >
      UnPublish
    </button>
    <button v-else class="badge badge-primary mr-2"
      @click="updatePublished(true)"
    >
      Publish
    </button>

    <button type="submit" class="btn btn-danger"
      @click="deleteTutorial"
    >
      Delete
    </button>

    <button type="submit" class="btn btn-success"
      @click="updateTutorial"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Tutorial...</p>
  </div>
</template>

<script>
import TutorialDataService from "../services/TutorialDataService";

export default {
  name: "tutorial",
  data() {
    return {
      currentTutorial: null,
      message: ''
    };
  },
  methods: {
    getTutorial(id) {
      TutorialDataService.get(id)
        .then(response => {
          this.currentTutorial = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updatePublished(status) {
      var data = {
        id: this.currentTutorial.id,
        title: this.currentTutorial.pbs_code,
        description: this.currentTutorial.install_meter_nos,
        status: this.currentTutorial.capacity_of_install_meter
      };

      TutorialDataService.update(this.currentTutorial.id, data)
        .then(response => {
          this.currentTutorial.published = status;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updateTutorial() {
      TutorialDataService.update(this.currentTutorial.id, this.currentTutorial)
        .then(response => {
          console.log(response.data);
          this.message = 'The info was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteTutorial() {
      TutorialDataService.delete(this.currentTutorial.id)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "netmeterlist" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getTutorial(this.$route.params.id);
  }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>