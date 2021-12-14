<template>
  <div>
    <input type="number" placeholder="Pesquisar por número de registro" id="search" v-model="search" required>
    <button v-on:click="fetchReg(search)" id="button">Pesquisar</button>
    <h3 v-if="mensage !== 'Sucesso'" class="show-text">{{ mensage }}</h3>
    <div v-if="mensage === 'Sucesso'">
        <div class="card" v-for="item in reg_ans" v-bind:key="item">  
            <div class="card-body">
                <h3>Registro ANS: {{ item.REG_ANS }}</h3>
            </div>
        </div>
    </div>
    <div v-show="loading" class="spinner"></div>
  </div>
</template>

<script>

export default {
  name: 'ListRegAns',
  data() {
      return {
          reg_ans: [],
          search: '',
          mensage: '',
          loading: false
      }
  },

  methods: {
      fetchReg(param) {
          if(param != '') {
            this.loading = true;
            this.mensage = '';
            this.reg_ans = [];
            fetch(`http://127.0.0.1:5000/dados/${param}`)
                .then( res => res.json() )
                .then( res => {
                    this.reg_ans = res.data;
                    this.loading = false;
                    this.mensage = res.mensage;
                })
                .catch( err => console.log(err) )
          } else {
              this.mensage = 'Digite alguma coisa';
          }
      }
  },

  created() {
  }
}
</script>

<style>
.card {
    text-align: left;
    background-color: #ddd;
    border: 1px solid #bbb;
    margin: auto;
    margin-top: 10px;
    padding: 10px;
    width: 50vw;
}

#search {
    width: 20vw;
    height: 5vh;
    border-radius: 10px;
    border: 1px solid #ddd;
    padding: 5px 10px;
}

#button {
    width: 8vw;
    height: 7vh;
    border-radius: 10px;
    border: 1px solid #ddd;
    padding: 5px 10px;
    background-color: #ccc;
}

.show-text {
    margin-top: 10px;
}

.spinner {
    margin: 40px auto;
    border: 8px solid #cec;
    border-left-color: #6e6;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}
</style>
