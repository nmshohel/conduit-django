<template>
<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
  <div class="form-group d-flex justify-content-center">

                                               <table class="table table-hover table-bordered" id="example">
                                                <thead>
                                                  <tr>
                                                    <th>ID</th>
                                                    <th>Pbs Code</th>
                                                    <th>consumer_nos</th>
                                                    <th>solar_panel_capacity</th>
                                                  </tr>
                                                </thead>
                                                <tbody >

                                                 <tr v-for="item in cstations" :key="item.id" v-if="item.pbs_code == currentUser.office_code || currentUser.user_role=='admin' ">
                                                 <td>{{item.id}}</td>
                                                    <td>{{item.pbs_code}}</td>
                                                    <td>{{item.charging_station_nos}}</td>
                                                    <td>{{item.charging_station_capacity}}</td>
                                                  </tr>

                                                </tbody>
                                              </table>




                          </div>

</template>

<script>
//Bootstrap and jQuery libraries
import 'bootstrap/dist/css/bootstrap.min.css'; //for table good looks
import 'jquery/dist/jquery.min.js';
//Datatable Modules
import "datatables.net-dt/js/dataTables.dataTables"
import "datatables.net-dt/css/jquery.dataTables.min.css"
import "datatables.net-buttons/js/dataTables.buttons.js"
import "datatables.net-buttons/js/buttons.colVis.js"
import "datatables.net-buttons/js/buttons.flash.js"
import "datatables.net-buttons/js/buttons.html5.js"
import "datatables.net-buttons/js/buttons.print.js"
import $ from 'jquery';
import axios from 'axios'; //for api calling



export default {
computed: {
    currentUser() {
      return this.$store.state.auth.user;
    }
  },

  mounted(){
    //Web api calling for dynamic data and you can also use into your demo project
    axios
    .get("http://127.0.0.1:8000/api/v1/gridchargingstation_info/")
    .then((res)=>
    {
      this.cstations = res.data;
      setTimeout(function(){
      $('#example').DataTable(
          {
              pagingType: 'full_numbers',
                pageLength: 5,
                processing: true,
                dom: 'Bfrtip',
                    buttons: ['copy', 'csv', 'print'
                    ]
          }
      );
      },
        1000
        );
    })
  },
  data: function() {
        return {
            cstations:[]
        }
    },
}
</script>