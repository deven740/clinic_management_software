import React, { useEffect, useState } from "react";
import PropTypes from "prop-types";
import { useTheme } from "@mui/material/styles";
import AppBar from "@mui/material/AppBar";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import axios from "axios";
import { format, addDays, parseISO } from "date-fns";
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

const backendURL = process.env.REACT_APP_BACKEND_URL;

function a11yProps(index) {
  return {
    id: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`,
  };
}

const createDatesArray = () => {
  const datesArray = [];
  const today = new Date();

  for (let i = 0; i < 7; i++) {
    datesArray.push(format(addDays(today, i), "yyyy-MM-dd"));
  }

  return datesArray;
};

// const showAppointments = (doctorID, value) => {
//   // return <Button variant="outlined">helo</Button>;
//   // console.log(doctorID, value, datesArray[value]);
//   const data = {
//     appointment_date: datesArray[value],
//     doctor_id: doctorID["id"],
//   };
//   // console.log(data);
//   // const fetchAppointmentsByDateAndDoctor = async (e) => {
//   //   try {
//   //     // const response = await axios.post(
//   //     //   `${backendURL}/appointments/filter-appointments-by-doctor-and-date`,
//   //     //   data
//   //     // );
//   //     // const responseData = response.data;
//   //     // console.log(responseData);
//   //     return <Button variant="outlined">helo</Button>;
//   //     // <Box sx={{ p: 3 }}>
//   //     //   <Stack spacing={2} direction="row">
//   //     //     {/* <Button variant="text" value="1">
//   //     //       Text
//   //     //     </Button>
//   //     //     <Button variant="contained" value="2">
//   //     //       Contained
//   //     //     </Button>
//   //     //     <Button variant="outlined" value="3">
//   //     //       Outlined
//   //     //     </Button> */}
//   //     //   </Stack>
//   //     // </Box>
//   //     // const resultArray = responseData.map((elm) => ({
//   //     // }));
//   //     // const data = responseData.map((elm) => {
//   //     //   return <Button variant="outlined">helo</Button>;
//   //     // });
//   //     // console.log(data);
//   //     // return data;
//   //   } catch (err) {
//   //     console.log(err);
//   //   }
//   // };
//   // fetchAppointmentsByDateAndDoctor();
//   // return (
//   //   <Box sx={{ p: 3 }}>
//   //     <Stack spacing={2} direction="row">
//   //       <Button variant="text" value="1">
//   //         Text
//   //       </Button>
//   //       <Button variant="contained" value="2">
//   //         Contained
//   //       </Button>
//   //       <Button variant="outlined" value="3">
//   //         Outlined
//   //       </Button>
//   //     </Stack>
//   //   </Box>
//   // );
// };

export default function FullWidthTabs(props) {
  const theme = useTheme();
  const datesArray = createDatesArray();
  const [value, setValue] = useState(0);
  const [appointmentSlots, setAppointmentSlots] = useState(null);

  useEffect(() => {
    const data = {
      appointment_date: datesArray[value],
      doctor_id: props.doctorID["id"],
    };

    const fetchAppointmentsByDateAndDoctor = async (e) => {
      try {
        const response = await axios.post(
          `${backendURL}/appointments/filter-appointments-by-doctor-and-date`,
          data
        );
        let responseData = response.data;
        // console.log(responseData);

        responseData = responseData.map((data) => ({
          ...data,
          clicked: false,
        }));

        setAppointmentSlots(responseData);
      } catch (err) {
        console.log(err);
      }
    };

    fetchAppointmentsByDateAndDoctor();

    return () => {};
  }, [value]);

  const handleChange = (event, newValue) => {
    // console.log(datesArray[newValue]);
    setValue(newValue);
  };

  const handleSlotClick = (event, key) => {
    // setAppointmentSlots((previous) => {
    //   previous.map((obj, id) => {
    //     if (key === id) {
    //       console.log("clicked");
    //       return { ...obj, clicked: true };
    //     }
    //     return { ...obj, clicked: false };
    //   });
    // });

    setAppointmentSlots((current) =>
      current.map((obj, id) => {
        if (key === id) {
          return { ...obj, clicked: true };
        }

        return { ...obj, clicked: false };
      })
    );
  };

  return (
    <Box sx={{ bgcolor: "background.paper", width: 500 }}>
      <AppBar position="static">
        <Tabs
          value={value}
          onChange={handleChange}
          indicatorColor="secondary"
          textColor="inherit"
          aria-label="full width tabs example"
          variant="scrollable"
          scrollButtons="auto"
        >
          {datesArray.map((date, key) => {
            return <Tab label={date} {...a11yProps(key)} key={key} />;
          })}
        </Tabs>
      </AppBar>
      <Box sx={{ p: 3 }}>
        <Stack spacing={2} direction="row">
          {appointmentSlots
            ? appointmentSlots.map((slot, key) => {
                return (
                  <Button
                    variant={slot.clicked ? "contained" : "outlined"}
                    key={key}
                    onClick={(event) => handleSlotClick(event, key)}
                    value={slot.id}
                  >
                    {slot.appointment_slot}
                  </Button>
                );
              })
            : ""}
        </Stack>
      </Box>
    </Box>
  );
}
