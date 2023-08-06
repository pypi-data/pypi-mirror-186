from ..core.constants import ShippingPartnerCodes as Partner

PARCEL_ERROR_CODE_PREFIX = 249000


class ParcelStatus:
    """ 包裹状态 """
    INIT = 'init'  # 初始   待上架
    CANCEL = 'cancel'  # 取消打包
    CHECKING = 'checking'  # 上架待揽收
    CHECKED = 'checked'  # 已揽收

    PARCEL_STAUTS_CHOICES = {
        INIT: "待上架",
        CANCEL: "取消打包",
        CHECKING: "待揽收",
        CHECKED: "已揽收"
    }


class ParcelEventConstKey:
    FROM_STATUS_LIST_KEY = 'from_status_list'
    TO_STATUS_KEY = 'to_status'
    TO_STATE_MAP_KEY = 'to_state_map'


class ParcelEventConst:
    NEW_ADD = 'new_add'
    CANCEL = 'cancel'  # 取消打包
    CHECKING = 'checking'  # 上架
    CHECKED = 'checked'  # 揽收
    TRANSFER_INACTIVE = 'transfer_inactive'  # 提交召回
    BULK_CHECKING = 'bulk_checking'  # 批量上架

    FROM_TO_MAP = {
        NEW_ADD: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.INIT, ParcelStatus.CANCEL,
            ],
            ParcelEventConstKey.TO_STATUS_KEY: ParcelStatus.INIT
        },
        CANCEL: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.INIT, ParcelStatus.CHECKING
            ],
            ParcelEventConstKey.TO_STATUS_KEY: ParcelStatus.CANCEL
        },
        CHECKING: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.INIT
            ],
            ParcelEventConstKey.TO_STATUS_KEY: ParcelStatus.CHECKING
        },
        BULK_CHECKING: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.INIT
            ],
            ParcelEventConstKey.TO_STATUS_KEY: ParcelStatus.CHECKING
        },
        CHECKED: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.CHECKING
            ],
            ParcelEventConstKey.TO_STATUS_KEY: ParcelStatus.CHECKED
        },
        TRANSFER_INACTIVE: {
            ParcelEventConstKey.FROM_STATUS_LIST_KEY: [
                ParcelStatus.CHECKING, ParcelStatus.CANCEL, ParcelStatus.INIT
            ],
            ParcelEventConstKey.TO_STATUS_KEY: None
        }
    }

    EVENT_TO_BUTTON_MAP = {
        NEW_ADD: "包裹打包",
        CANCEL: "包裹取消打包",
        CHECKING: "包裹上架",
        BULK_CHECKING: "批量上架",
        CHECKED: "包裹揽收",
        TRANSFER_INACTIVE: "包裹召回",
    }


class ParcelSource:
    ONLINE_SOURCE = 'online'  # 在线发货
    AFTERSALE_RETURN = 'afs_return'  # 退货寄回
    EXCHANGE_RETURN = 'ex_return'  # 换货寄回


class TransferStatus:
    """ 交接记录状态 """
    ACTIVE = "active"  # 已上架
    INACTIVE = 'inactive'  # 已召回

    TRANSFER_STAUTS_CHOICES = {
        ACTIVE: "已上架",
        INACTIVE: "已召回",
    }


class TransferEventConstKey:
    FROM_STATUS_LIST_KEY = 'from_status_list'
    TO_STATUS_KEY = 'to_status'
    TO_STATE_MAP_KEY = 'to_state_map'


class TransferEventConst:
    NEW_ADD = 'new_add'
    INACTIVE = 'inactive'

    FROM_TO_MAP = {
        NEW_ADD: {
            TransferEventConstKey.FROM_STATUS_LIST_KEY: [
                TransferStatus.ACTIVE,
            ],
            TransferEventConstKey.TO_STATUS_KEY: None,
        },
        INACTIVE: {
            TransferEventConstKey.FROM_STATUS_LIST_KEY: [
                TransferStatus.ACTIVE,
            ],
            TransferEventConstKey.TO_STATUS_KEY: TransferStatus.INACTIVE,
        }
    }

    EVENT_TO_BUTTON_MAP = {
        NEW_ADD: "建立交接档案",
        INACTIVE: "交接档案召回",
    }


class ExpressName:
    """ 包裹管理中给前端用的快递公司 """

    SF = 'sf'
    YZ = 'yz'
    ZTO = 'zto'
    JD = 'jd'

    CODE_2_system_codes = {
        SF: [Partner.SF, Partner.SFTCJS],
        YZ: [Partner.YZPY],
        ZTO: [Partner.ZTO],
        JD: [Partner.JD],
    }

    CODE_2_NAME_MAP = {
        SF: "顺丰",
        YZ: "邮政",
        ZTO: "中通",
        JD: "京东",
    }

    EXPRESS_NAME_INFOS = [
        {
            "name": CODE_2_NAME_MAP[SF],
            "code": SF,
        },
        {
            "name": CODE_2_NAME_MAP[YZ],
            "code": YZ,
        },
        {
            "name": CODE_2_NAME_MAP[ZTO],
            "code": ZTO,
        },
        {
            "name": CODE_2_NAME_MAP[JD],
            "code": JD,
        },
    ]
