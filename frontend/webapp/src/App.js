import React from "react";
import { Provider, useDispatch } from "react-redux";
import { configureStore } from "@reduxjs/toolkit";
import { taskMiddleware } from "react-palm/tasks";

import KeplerGl from "kepler.gl";
import { addDataToMap } from "kepler.gl/actions";
import keplerGlReducer from "kepler.gl/reducers";

import useSwr from "swr";

const store = configureStore({
  reducer: {
    keplerGl: keplerGlReducer,
  },
  middleware: [taskMiddleware],
});

function App() {
  return (
    <Provider store={store}>
      <Map />
    </Provider>
  );
}

function Map() {
  return (
    <KeplerGl
      id="covid"
      mapboxApiAccessToken={
        "pk.eyJ1Ijoic2l3YXRjaGFpcmF0IiwiYSI6ImNsMmxjZW5yZTB6engzaW53dmc5Y3FlZzMifQ.NanT0HoZXtIwWkgWhRXp_A"
      }
      width={window.innerWidth}
      height={window.innerHeight}
    />
  );
}

export default App;
