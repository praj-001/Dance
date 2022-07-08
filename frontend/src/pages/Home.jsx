import "./Home.css";

const Home = () => {
  return (
    <div>
      <div className= "container">
        <h3>Generate Meet Link</h3>
        <div className="Home">
          <input className = "Text" type="text" />
          <button className = "Button"> Generate </button>
        </div>
      </div>

      <div className = "About">
        <h3> About </h3>
        <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis volutpat metus, vitae lacinia mi. Donec ut fringilla mi, quis dictum nunc. Morbi sollicitudin nulla enim, eget tempor dolor egestas ut. Duis facilisis enim ut orci hendrerit scelerisque. In laoreet ultricies nisl, vel porta tortor sagittis a.</p>
      </div>
      
    </div>
    
    
  );
};
export default Home;