file(GLOB xml ${CMAKE_CURRENT_SOURCE_DIR}/*.xml)
file(GLOB ini ${CMAKE_CURRENT_SOURCE_DIR}/*.ini)


# Option to install all iRonCub robots
option(INSTALL_ALL_IRONCUB_VERSIONS "Install all variations of iRonCub robots." TRUE)

if(INSTALL_ALL_IRONCUB_VERSIONS)
    set(robot_list iRonCub-Mk3 iRonCub-Mk3-FT-ARMS) #Add to the list other iRonCub3 versions (that share the same configuration files)
    set(robot_list iRonCub-Mk3 iRonCub-Mk3-WALKING-TURBINES) #Add to the list other iRonCub3 versions (that share the same configuration files)
else()
    set(robot_list iRonCub-Mk3) #install only iRonCub-Mk3
endif()

foreach(appname IN LISTS robot_list)
    file(GLOB xml ${CMAKE_CURRENT_SOURCE_DIR}/*.xml)
    file(GLOB ini ${CMAKE_CURRENT_SOURCE_DIR}/*.ini)
    yarp_install(FILES ${xml} DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(FILES ${ini} DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY estimators DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY calibrators DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY wrappers DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY hardware DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY sensors  DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
    yarp_install(DIRECTORY telemetry  DESTINATION ${ICUBCONTRIB_ROBOTS_INSTALL_DIR}/${appname})
endforeach()
