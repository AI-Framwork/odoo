/** @crossnow-module **/

export const session = crossnow.__session_info__ || {};
delete crossnow.__session_info__;
