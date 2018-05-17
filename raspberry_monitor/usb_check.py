import subprocess as sp

__keyboard_ids = ['keyboard']
__mouse_ids = ['mouse']
__camera_ids = ['camera','video']

usb_info = sp.check_output(['lsusb','-v']).lower()

has_keyboard = lambda: any([ k in usb_info for k in __keyboard_ids])
has_mouse = lambda: any([m in usb_info for m in __mouse_ids])
has_camera = lambda: any([c in usb_info for c in __camera_ids])

if __name__ == '__main__':
	print(	"Keyboard Present:\t{}\n".format(has_keyboard()) +
		"Mouse Present:\t{}\n".format(has_mouse()) +
		"Camera Present:\t{}\n".format(has_camera())
		)

