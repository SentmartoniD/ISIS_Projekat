import { useState } from "react";
import { Pelda } from "../services/FrontPageService";

function FrontPage(){
    const [loadData, setLoadData] = useState([]);
    const [weatherData, setWeatherData] = useState();
    const [usHolidaysData, setUSHolidaysData] = useState();

    const handleFilesChange1 = (event) => {
        const files = event.target.files;
        const filesArray = Array.from(files);
        setLoadData(filesArray);
        console.log(filesArray);
      };
      const handleFilesChange2 = (event) => {
        const files = event.target.files;
        const filesArray = Array.from(files);
        setWeatherData(filesArray);
        console.log(filesArray);
      };

      const handleSubmitTrainModel = async (e) =>{
        try{
            const response = await Pelda();
            console.log(response)
        } catch(error){
            if (!error?.response)
                alert("No server response!")
            else
                alert(JSON.stringify(error.response.data))
        }
      }

      const handleSubmitBeginForecast = async (e) =>{

      }

    return(
        <section className="frontpage-section" >
            <h1 className="frontpage-h1" >Electricity consumption forecast</h1>
            <div className="frontpage-div-control" > 
                <div className="frontpage-div2" >
                    <label className="frontpage-label" >Load data</label>
                    <input type="file" multiple directory="true" webkitdirectory="true" onChange={handleFilesChange1} ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >Weather data</label>
                    <input type="file" multiple onChange={handleFilesChange2} ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >US holidays data</label>
                    <input type="file" onChange={(e) => setUSHolidaysData(e.target.value)} ></input>
                </div>
                <button className="frontpage-button" onClick={handleSubmitTrainModel} >TRAIN MODEL</button>
                <button className="frontpage-button" onClick={handleSubmitBeginForecast} >BEGIN FORECAST</button>
            </div>
        </section>
    )
}




export default FrontPage;