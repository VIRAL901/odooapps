/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { FormViewDialog } from "@web/views/view_dialogs/form_view_dialog";
import { useCommand } from "@web/core/commands/command_hook";
import { useService } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { registry } from "@web/core/registry";
import { isIosApp } from "@web/core/browser/feature_detection";
import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { jsonrpc } from "@web/core/network/rpc_service";
import { browser } from "@web/core/browser/browser";
import { useDebounced } from "@web/core/utils/timing";

patch(ActivityMenu.prototype, {
    setup() {
        var self = this;
        this.bcameraAccess = this.cameraAccess();
        if (this.bcameraAccess) {
            console.log('Camera access is allowed.');
        } else{
            console.log('Camera access is denied.');
        }
        this.onClickVideoOn = useDebounced(this.FaceVideoOn, 200, true);
        return super.setup(...arguments);
    },
    async cameraAccess() {
        const permissionStatus = await navigator.permissions.query({ name: 'camera' });
        if (permissionStatus.state === 'granted') {
            return true;
        }else{
            return false;
        }
    },
    async FaceVideoOn(){
        var video = document.querySelector('.videostream');
        this.bcameraAccess = await this.cameraAccess();
        if(this.bcameraAccess && video){
            navigator.mediaDevices.getUserMedia({ video: true }).then(function(mediaStream) {
                if(video){
                    video.srcObject = mediaStream;
                    video.play();
                }
            });

        }
    },
    async searchReadEmployee(){
        this.bcameraAccess = await this.cameraAccess();
        var result = await super.searchReadEmployee(...arguments);
        return result;
    },
    async signInOut() {
        var result = {};
        this.bcameraAccess = await this.cameraAccess();
        if(this.bcameraAccess){
            var video = document.querySelector('.videostream');
            var img = document.querySelector('#screenshot-img');
            window.canvas = document.createElement('canvas');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            canvas.getContext('2d').drawImage(video, 0, 0);
            img.src = canvas.toDataURL('image/webp');
            // iOS app lacks permissions to call `getCurrentPosition`
            if (!isIosApp()) {
                navigator.geolocation.getCurrentPosition(
                    async ({coords: {latitude, longitude}}) => {
                        result = await this.rpc("/update_attandance", {
                            'latitude':latitude,
                            'longitude':longitude,
                            'check_in':!this.state.checkedIn,
                            'check_in_out_image':img.src
                        })
                        await this.searchReadEmployee()
                    },
                    async err => {
                        result = await this.rpc("/update_attandance",{
                                'check_in':!this.state.checkedIn,
                                'check_in_out_image':img.src
                            })
                        await this.searchReadEmployee()
                    },
                    {
                        enableHighAccuracy: true,
                    }
                )
            } else {
                result = await this.rpc("/update_attandance",{
                                'check_in':!this.state.checkedIn,
                                'check_in_out_image':img.src
                            })
                await this.searchReadEmployee()
            }
        }else{
            // iOS app lacks permissions to call `getCurrentPosition`
            if (!isIosApp()) {
                navigator.geolocation.getCurrentPosition(
                    async ({coords: {latitude, longitude}}) => {
                        await this.rpc("/hr_attendance/systray_check_in_out", {
                            latitude,
                            longitude
                        })
                        await this.searchReadEmployee()
                    },
                    async err => {
                        await this.rpc("/hr_attendance/systray_check_in_out")
                        await this.searchReadEmployee()
                    },
                    {
                        enableHighAccuracy: true,
                    }
                )
            } else {
                await this.rpc("/hr_attendance/systray_check_in_out")
                await this.searchReadEmployee()
            }
        }

    },
    destroy: function() {
        var video = document.querySelector('.videostream');
        if (video) {
            video.srcObject.getTracks().forEach(function(track) {
                track.stop();
            })
            video.pause();
            delete window.canvas;
        }
    },
});
