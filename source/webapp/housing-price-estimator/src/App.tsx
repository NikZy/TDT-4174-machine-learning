import React, { useState } from 'react';
import './App.css';
import { features as Features } from 'process';
import { Controller, useForm } from 'react-hook-form';
import { Button, Input, Slider } from '@material-ui/core';
import styled from 'styled-components';
import './assets/css/main.css';
import videoClip from './images/banner.mp4';
// import './assets/sass/main.scss';
import bannerImage from './images/banner.jpg';
import bg1 from './images/bg.jpg';

const ApiPost = (url, data) =>
  fetch(`http://localhost:5000/` + url, {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  }).then((res) => res.json());
function App() {
  const { register, handleSubmit, watch, errors, control } = useForm();
  const [estimatedPrice, setEstimatedPrice] = useState<number>();
  const predictedPriceTest = estimate_price(normalizeParameters(test));
  const onSubmit = (data) => {
    console.log('Data:');
    const dataConvertedToInts = convertIntObj(data);
    console.log(convertIntObj(data));
    data.lastFixed = calculateLastFixed(data.year_built, data.year_renovated);
    data.center_distance = calculateCenterDistance(
      data.latitude,
      data.longitude
    );
    const features = Object.assign(test, dataConvertedToInts);
    console.log(features);
    ApiPost('estimator', features)
      .then((res) => setEstimatedPrice(res.prediction))
      .catch((err) => console.log(err));
  };
  return (
    <html>
      <head>
        <title>Industrious by TEMPLATED</title>
        <meta charSet="utf-8" />
        <meta
          name="viewport"
          content="width=device-width, initial-scale=1, user-scalable=no"
        />
        <meta name="description" content="" />
        <meta name="keywords" content="" />
      </head>
      <body className="is-preload">
        <header id="header">
          <a className="logo" href="index.html">
            Industrious
          </a>
          <nav></nav>
        </header>

        <PosterHeader></PosterHeader>
        <section className="wrapper">
          <div className="inner">
            <header className="special">
              <h2>House Price estimator for King County</h2>
              <p>
                Type in features about the house, and we will give you and
                estimated price.
              </p>
            </header>
            <div className="highlights">
              <FormContainer>
                <form onSubmit={handleSubmit(onSubmit)}>
                  <InputContainer>
                    Bedrooms
                    <Input
                      type="number"
                      name="bedrooms"
                      defaultValue="3"
                      inputRef={register({ required: true })}
                    />
                    {errors.bedroom && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    Grade
                    <Input
                      type="number"
                      name="grade"
                      defaultValue="7"
                      inputRef={register({ required: true })}
                    />
                    {errors.number && <span>This field is required</span>}
                  </InputContainer>

                  <InputContainer>
                    Bathrooms
                    <Input
                      type="number"
                      name="bathrooms"
                      defaultValue="1"
                      inputRef={register({ required: true })}
                    />
                    {errors.bathrooms && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    sqft_living
                    <Input
                      type="number"
                      name="sqft_living"
                      defaultValue="1180"
                      inputRef={register({ required: true })}
                    />
                    {errors.sqft_living && <span>This field is required</span>}
                  </InputContainer>

                  <InputContainer>
                    sqft_lot
                    <Input
                      type="number"
                      name="sqft_lot"
                      defaultValue="5650"
                      inputRef={register({ required: true })}
                    />
                    {errors.sqft_lot && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    waterfront
                    <Input
                      type="number"
                      name="waterfront"
                      defaultValue="0"
                      inputRef={register({ required: true })}
                    />
                    {errors.waterfront && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    floors
                    <Input
                      type="number"
                      name="floors"
                      defaultValue="1"
                      inputRef={register({ required: true })}
                    />
                    {errors.floors && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    view
                    <Input
                      type="number"
                      name="view"
                      defaultValue="0"
                      inputRef={register({ required: true })}
                    />
                    {errors.view && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    condition
                    <Input
                      type="number"
                      name="condition"
                      defaultValue="3"
                      inputRef={register({ required: true })}
                    />
                    {errors.condition && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    sqft_above
                    <Input
                      type="number"
                      name="sqft_above"
                      defaultValue="1180"
                      inputRef={register({ required: true })}
                    />
                    {errors.sqft_above && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    sqft_basement
                    <Input
                      type="number"
                      name="sqft_basement"
                      defaultValue="0"
                      inputRef={register({ required: true })}
                    />
                    {errors.sqft_basement && (
                      <span>This field is required</span>
                    )}
                  </InputContainer>
                  <InputContainer>
                    zip_code
                    <Input
                      type="number"
                      name="zip_code"
                      defaultValue="98178"
                      inputRef={register({ required: true })}
                    />
                    {errors.zip_code && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    latitude
                    <Input
                      type="number"
                      name="latitude"
                      defaultValue="47.5112"
                      inputRef={register({ required: true })}
                    />
                    {errors.latitude && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    longitude
                    <Input
                      type="number"
                      name="longitude"
                      defaultValue="-122.257"
                      inputRef={register({ required: true })}
                    />
                    {errors.longitude && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    year_built
                    <Input
                      type="number"
                      name="year_built"
                      defaultValue="1995"
                      inputRef={register({ required: true })}
                    />
                    {errors.year_built && <span>This field is required</span>}
                  </InputContainer>
                  <InputContainer>
                    year_renovated
                    <Input
                      type="number"
                      name="year_renovated"
                      defaultValue="0"
                      inputRef={register({ required: true })}
                    />
                    {errors.year_renovated && (
                      <span>This field is required</span>
                    )}
                  </InputContainer>
                  <InputContainer>
                    <Button name="submit" color="primary" type="submit">
                      Submit
                    </Button>
                  </InputContainer>
                </form>
                <h2>Estimated price:</h2>
                <h1>{predictedPriceTest ? estimatedPrice : 0}</h1>
              </FormContainer>
            </div>
          </div>
        </section>

        <section id="cta" className="wrapper">
          <div className="inner">
            {/*             <h2>Curabitur ullamcorper ultricies</h2>
            <p>
              Nunc lacinia ante nunc ac lobortis. Interdum adipiscing gravida
              odio porttitor sem non mi integer non faucibus ornare mi ut ante
              amet placerat aliquet. Volutpat eu sed ante lacinia sapien lorem
              accumsan varius montes viverra nibh in adipiscing. Lorem ipsum
              dolor vestibulum ante ipsum primis in faucibus vestibulum. Blandit
              adipiscing eu felis iaculis volutpat ac adipiscing sed feugiat eu
              faucibus. Integer ac sed amet praesent. Nunc lacinia ante nunc ac
              gravida.
            </p> */}
          </div>
        </section>

        <footer id="footer">
          <div className="inner">
            <div className="content">
              <section>
                <h3>About this project</h3>
                <p>
                  The site uses a Linear Regression model. The modell is trained
                  on this dataset from
                  <a href="https://www.kaggle.com/harlfoxem/housesalesprediction">
                    https://www.kaggle.com/harlfoxem/housesalesprediction
                  </a>
                  .
                </p>
              </section>
              <section>
                <h4>Group members</h4>
                <ul className="alt">
                  <li>Sindre J.I Sivertsen (sjsivert)</li>
                  <li>Eivind Emil Floer (eivinf)</li>
                  <li>Brage Lytskjold (bragelyt)</li>
                </ul>
              </section>
            </div>
            <div className="copyright">
              &copy; Untitled. Photos <a href="https://unsplash.co">Unsplash</a>
              , Video <a href="https://coverr.co">Coverr</a>.
            </div>
          </div>
        </footer>

        <script src="assets/js/jquery.min.js"></script>
        <script src="assets/js/browser.min.js"></script>
        <script src="assets/js/breakpoints.min.js"></script>
        <script src="assets/js/util.js"></script>
        <script src="assets/js/main.js"></script>
      </body>
    </html>
  );
}

const PosterHeader = styled.div`
  width: 100%;
  height: 400px;
  background-color: #111111;
  background-image: linear-gradient(
      rgba(0, 0, 0, 0.75),
      rgba(206, 27, 40, 0.25)
    ),
    url(${bg1});
`;
const FormContainer = styled.div`
  display: flex;
  margin: 0 auto;
  max-width: 100rem;
  flex-direction: column;
`;

const InputContainer = styled.div`
  display: flex;
  align-self: flex-end;
  justify-content: space-between;
`;
const calculateCenterDistance = (lat: number, long: number): number => {
  const latCenter = 47.63;
  const longCenter = -122.2;
  return (lat - latCenter) ** 2 + (long - longCenter) ** 2;
};

const calculateLastFixed = (built: number, renovate: number) => {
  // hva gjøres her?
  /*     lastFixedList[i] = (2020 - max(df.at[i, 'yr_built'],
                                   df.at[i, 'yr_renovated'])) / df.at[i, 'sqft_living'] */
  return 2020 - Math.max(built, renovate);
};

function convertIntObj(obj) {
  const res = {};
  for (const key in obj) {
    const parsed = parseInt(obj[key]);
    res[key] = parsed;
    res[key] = isNaN(parsed) ? obj[key] : parsed;
  }
  return res;
}
interface Features {
  bathrooms: number;
  bedrooms: number;
  sqft_living: number;
  sqft_lot: number;
  waterfront: number;
  floors: number;
  view: number;
  condition: number;
  grade: number;
  sqft_above: number;
  sqft_basement: number;
  zip_code: number;
  sqft_living15: number;
  sqft_lot15: number;
  center_distance: number;
  last_fixed: number;
}

const test: Features = {
  bathrooms: 1,
  bedrooms: 3,
  sqft_living: 1180,
  sqft_lot: 5650,
  floors: 1,
  waterfront: 0,
  view: 0,
  condition: 3,
  grade: 7,
  sqft_above: 1180,
  sqft_basement: 0,
  last_fixed: calculateLastFixed(1955, 0),
  zip_code: 98178,
  sqft_living15: 1340,
  sqft_lot15: 5650,
  center_distance: calculateCenterDistance(47.5112, -122.257),
};
/* const test2: Features = {
  bedrooms: 2,
  bathrooms: -0.3987371485515761,
  sqft_living:-1.4474635685648216,
  sqft_lot: -0.9036171393191288,
  floors: -0.1287548306162246,
  waterfront: -0.9154270041565511,
  view: -0.08717263102067989,
  condition: -0.30575946383494007,
  grade: 0.9075535361389149,
  sqft_above: -0.5588357490736213,
  -0.6501739072174175,-0.6586810403679764,-1.400644831402753,-1.0308984565214254,-0.14351452261811226,-1.3417547735375033,0.41231859187110054 */
const normalizeParameters = (variables: Features): Features => {
  // subracting the average
  // dividing by standard deviation
  return {
    bedrooms: (variables.bedrooms - 3.370842) / 0.930062,
    bathrooms: (variables.bathrooms - 2.114757) / 0.770163,
    sqft_living: (variables.sqft_living - 2079.9) / 918.44089,
    sqft_lot: (variables.sqft_lot - 15106.97) / 41420.5,
    floors: (variables.floors - 1.494309) / 0.539989,
    waterfront: (variables.waterfront - 0.007542) / 0.086517,
    view: (variables.view - 0.234303) / 0.766318,
    condition: (variables.condition - 3.40943) / 0.650743,
    grade: (variables.grade - 7.656873) / 1.175459,
    sqft_above: (variables.sqft_above - 1788.39) / 828.1,
    sqft_basement: (variables.sqft_basement - 291.51) / 442.575043,
    zip_code: (variables.zip_code - 98077.94) / 53.51,
    sqft_living15: (variables.sqft_living15 - 1986.55) / 685.4,
    sqft_lot15: (variables.sqft_lot15 - 12768.45) / 27304.18,
    center_distance: (variables.center_distance - 0.18773) / 0.094203,
    last_fixed: (variables.last_fixed - 0.029588) / 0.027193,
  };
};
const estimate_price = (variables: Features): number => {
  return (
    -12064.4943 * variables.bedrooms +
    16860.5256 * variables.bathrooms + // bathrooms
    60003.3306 * variables.sqft_living + // sqft_living
    22816.4262 * variables.sqft_lot + // sqft_lot
    19683.5599 * variables.floors + // floors
    53372.09013601506 * variables.waterfront + //waterfont
    37140.0533 * variables.view + // view
    19984.0531 * variables.condition + //  condition
    98687.6017 * variables.grade + // grade
    48484.0553 * variables.sqft_above + // sqft_above
    33802.8639 * variables.sqft_basement + // sqft_basement code
    4503.30596 * variables.zip_code + //zip
    17992.5267 * variables.sqft_living15 + //  sqft_living15
    -18066.3354 * variables.sqft_lot15 + // sqft_sqft_lot15
    91977.8574 * variables.center_distance + // center_distance
    60023.9138 * variables.last_fixed + //  last_fixed
    524327 * 1
  );
};

export default App;
