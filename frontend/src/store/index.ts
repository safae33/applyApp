import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    apiUrl: "192.168.2.133:5000",
    isAuth: false,
    errMessage: "",
    applyArr: [

    ],
    isAdmin: true,
    user: { isAdmin: false , id:0},
    allUsers: [],
    dataHere: true,

  },
  getters: {
    getApiUrl(state) {
      return state.apiUrl;
    },
    getIsAuth(state) {
      return state.isAuth;
    },
    getApplyArr(state) {
      return state.applyArr;
    },
    getIsAdmin(state) {
      return state.user.isAdmin;
    },
    getUsers(state) {
      return state.user.isAdmin;
    },
    getDataHere(state) {
      return state.dataHere;
    },
    getErrMessage(state) {
      return state.errMessage;
    },
    getAllUsers(state) {
      return state.allUsers;
    },
  },
  mutations: {

    setIsAuth(state, isAuth) {
      state.isAuth = isAuth;
    },
    setApplyArr(state, data) {
      state.applyArr = data;
    },
    setUser(state, data) {
      state.user = data;
    },
    setDataHere(state, data) {
      state.dataHere = data;
    },
    setErrMessage(state, data) {
      state.errMessage = data;
    },
    setAllUsers(state, data) {
      state.allUsers = data;
    },

  },
  actions: {
    setIsAuthAct({ commit }, isAuth) {
      commit('setIsAuth', isAuth);
    },
    async setApplyListApi({ commit, state }) {
      await axios
        .post("http://" + state.apiUrl + "/api/getAllApplies", { "isAdmin": state.user.isAdmin, "id": state.user.id })
        .then(response => {
          commit('setDataHere', false);
          commit('setApplyArr', response.data["result"]);
          console.log(state.applyArr)

        })
        .catch(error => {
          console.log(error);
        });
    },
    async check_user({ commit, state }, [mail, passwd]) {
      await axios
        .post("http://" + state.apiUrl + "/api/checkUser", { mail: mail, passwd: passwd })
        .then(response => {

          if (response.data["result"] == "0") {
            commit('setIsAuth', true);
            commit('setUser', response.data["data"]);
          }
          else {
            commit('setErrMessage', response.data["data"])
          }
        })
        .catch(error => {
          commit('setErrMessage', "Sunucu İle Bağlantı Kurulamadı.")
          console.log(error);
        });
    },

    async get_users({ commit, state }) {
      await axios
        .get("http://" + state.apiUrl + "/api/getUsers")
        .then(response => {
          commit('setAllUsers', response.data["result"]);
        })
        .catch(error => {
          console.log(error);
        });
    },
    async save_user({ state }, user) {
      await axios
        .post("http://" + state.apiUrl + "/api/addUser", { user: user })
        .then(response => {
          return response.data["result"];
        })
        .catch(error => console.log(error));
    },
    async delete_user({ state }, id) {
      await axios
        .post("http://" + state.apiUrl + "/api/delUser", { id: id })
        .then(response => {
          return response.data["result"];
        })
        .catch(error => console.log(error));
    },
  },
  modules: {
  }
})
