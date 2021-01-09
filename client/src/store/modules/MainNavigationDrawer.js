export default  {
  state : () => ({ sidebar: true }),

  mutations: { switchSidebar: (state) => {
    state.sidebar = !state.sidebar;
  }},
  
  getters: {
    getSidebar: (state) => {
      return state.sidebar;
    }
  }
}