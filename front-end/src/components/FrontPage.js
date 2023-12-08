


function FrontPage(){
    return(
        <section className="frontpage-section" >
            <h1 className="frontpage-h1" >Electricity consumption forecast</h1>
            <div className="frontpage-div-control" > 
                <div className="frontpage-div2" >
                    <label className="frontpage-label" >Load data</label>
                    <input type="file" ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >Weather data</label>
                    <input type="file" ></input>
                </div>
                <div className="frontpage-div2">
                    <label className="frontpage-label" >US holidays data</label>
                    <input type="file" ></input>
                </div>
                {/* CREATE MODEL BUTTON  */}
                {/* BEGIN FORECAST*/}
            </div>
        </section>
    )
}




export default FrontPage;