
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\shuffleboard\ShuffleboardComponent.h>

#include <frc/shuffleboard/ShuffleboardContainer.h>




namespace rpygen {

using namespace frc;


template <typename Derived>
struct bind_frc__ShuffleboardComponent {

    
    
    
    py::class_<typename frc::ShuffleboardComponent<Derived>, frc::ShuffleboardComponentBase> cls_ShuffleboardComponent;




    py::module &m;
    std::string clsName;

bind_frc__ShuffleboardComponent(py::module &m, const char * clsName) :
    cls_ShuffleboardComponent(m, clsName),



    m(m),
    clsName(clsName)
{
    
}

void finish(const char * set_doc = NULL, const char * add_doc = NULL) {

    
  cls_ShuffleboardComponent.doc() =
    "A generic component in Shuffleboard.\n"
"\n"
"@tparam Derived the self type";

  cls_ShuffleboardComponent
      .def("withProperties", &frc::ShuffleboardComponent<Derived>::WithProperties,
      py::arg("properties"), release_gil(), py::return_value_policy::reference_internal, py::doc(
    "Sets custom properties for this component. Property names are\n"
"case-sensitive and whitespace-insensitive (capitalization and spaces do not\n"
"matter).\n"
"\n"
":param properties: the properties for this component\n"
"\n"
":returns: this component")
  )
    
      .def("withPosition", &frc::ShuffleboardComponent<Derived>::WithPosition,
      py::arg("columnIndex"), py::arg("rowIndex"), release_gil(), py::return_value_policy::reference_internal, py::doc(
    "Sets the position of this component in the tab. This has no effect if this\n"
"component is inside a layout.\n"
"\n"
"If the position of a single component is set, it is recommended to set the\n"
"positions of *all* components inside a tab to prevent Shuffleboard\n"
"from automatically placing another component there before the one with the\n"
"specific position is sent.\n"
"\n"
":param columnIndex: the column in the tab to place this component\n"
":param rowIndex:    the row in the tab to place this component\n"
"\n"
":returns: this component")
  )
    
      .def("withSize", &frc::ShuffleboardComponent<Derived>::WithSize,
      py::arg("width"), py::arg("height"), release_gil(), py::return_value_policy::reference_internal, py::doc(
    "Sets the size of this component in the tab. This has no effect if this\n"
"component is inside a layout.\n"
"\n"
":param width:  how many columns wide the component should be\n"
":param height: how many rows high the component should be\n"
"\n"
":returns: this component")
  )
    
;

  

    if (set_doc) {
        cls_ShuffleboardComponent.doc() = set_doc;
    }
    if (add_doc) {
        cls_ShuffleboardComponent.doc() = py::cast<std::string>(cls_ShuffleboardComponent.doc()) + add_doc;
    }

    
}

}; // struct bind_frc__ShuffleboardComponent

}; // namespace rpygen